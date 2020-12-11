from datetime import timedelta

from rest_framework.generics import get_object_or_404

from trading_platform.celery import app
from app.models import Offer, Trade, Money, Inventory


@app.task
def offer_selection():
    offers = list(Offer.objects.all())
    offers_type_lists = offer_lists_creator(offers)
    offers_b_iter = iter(offers_type_lists[0])
    next_b_exist = True
    while next_b_exist:
        try:
            offer_b = next(offers_b_iter)
        except StopIteration:
            next_b_exist = False
        else:
            offers_s_iter = iter(Offer.objects.filter(type=0, is_active=True))
            suitable_offers = []
            next_s_exist = True
            while next_s_exist:
                try:
                    offer_s = next(offers_s_iter)
                except StopIteration:
                    next_s_exist = False
                else:
                    if is_offer_suitable(offer_b, offer_s):
                        suitable_offers.append(offer_s)
                    most_suitable = find_most_suitable_offer(suitable_offers)
                    make_trade(offer_b, most_suitable)


def find_suitable_offers(offer_b, offers):
    suitable_offers = []
    for offer_s in offers:
        if is_offer_suitable(offer_b, offer_s):
            suitable_offers.append(offer_s)
    if len(suitable_offers) != 0:
        most_s = find_most_suitable_offer(suitable_offers)
        make_trade(offer_b, most_s)


def make_trade(offer_b, offer_s):
    print("MAKING TRADE ON:", offer_b, offer_s)

    price_for_item_b = get_item_price(offer_b)
    price_for_item_s = get_item_price(offer_s)

    # If buy user's inventory doesn't exist - create
    if not Inventory.objects.filter(user=offer_b.user, item=offer_b.item).exists():
        inv = Inventory(user=offer_b.user, item=offer_b.item, amount=0)
        inv.save()
    amount = offer_b.amount if offer_b.amount <= offer_s.amount else offer_s.amount
    total_price = amount * get_item_price(offer_s)

    # Making trade
    trade = Trade(item=offer_b.item, amount=amount, price=total_price, \
                  seller=offer_s.user, seller_offer=offer_s, buyer=offer_b.user, \
                  buyer_offer=offer_b)

    # Offers & inventories amount actions
    offer_b.amount -= amount;
    offer_s.amount -= amount;

    # Changing inventory amount
    inventory_b = get_object_or_404(Inventory, user=offer_b.user, item=offer_b.item)
    inventory_s = get_object_or_404(Inventory, user=offer_s.user, item=offer_s.item)
    inventory_s.amount -= amount
    inventory_b.amount += amount

    # Money actions
    money_action(offer_b.user, amount, offer_b.item.currency_id, "-")
    money_action(offer_s.user, amount, offer_s.item.currency_id, "+")

    # Check if offer is closed
    if offer_b.amount == 0:
        offer_b.is_active = False
    if offer_s.amount == 0:
        offer_s.is_active = False

    offer_b.price = offer_b.amount * price_for_item_b;
    offer_s.price = offer_s.amount * price_for_item_s;

    # Saving all data
    trade.save()
    offer_b.save()
    offer_s.save()
    inventory_b.save()
    inventory_s.save()


def is_offer_suitable(offer_b, offer_s):
    if offer_b.user != offer_s.user and offer_b.item == offer_s.item and \
            get_item_price(offer_b) >= get_item_price(offer_s):
        return True
    else:
        return False


def get_item_price(offer):
    return offer.price / offer.amount


def find_most_suitable_offer(offers):
    response = offers[0]
    for offer in offers[1:]:
        if get_item_price(offer) < get_item_price(response):
            response = offer
    return response


def offer_lists_creator(offers_list):
    offers_sell = [offer for offer in offers_list if (offer.type == 0 and offer.is_active == True)]
    offers_buy = [offer for offer in offers_list if (offer.type == 1 and offer.is_active == True)]
    return [offers_buy, offers_sell]


def money_action(user, amount, currency, action):
    money = get_object_or_404(Money, user=user, currency_id=currency)
    if action == "-":
        money.money -= amount
    if action == "+":
        money.money += amount
    money.save()


app.conf.beat_schedule = {
    'offer-selection-in-10-sec': {
        'task': 'api.tasks.offer_selection',
        'schedule': timedelta(seconds=60),
    },
}
