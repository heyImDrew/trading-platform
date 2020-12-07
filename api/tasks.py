from datetime import timedelta

from rest_framework.generics import get_object_or_404

from trading_platform.celery import app
from app.models import Offer, Trade, Money, Inventory


@app.task
def offer_selection():
    offers = Offer.objects.all()
    offers_type_lists = offer_lists_creator(list(offers))
    offers_buy = offers_type_lists[0]
    offers_sell = offers_type_lists[1]
    for offer in offers_buy:
        find_suitable_offers(offer, offers_sell)


def money_action(user, amount, action):
    money = get_object_or_404(Money, user=user)
    if action == "-":
        money.money -= amount
    if action == "+":
        money.money += amount
    money.save()


def get_item_price(offer):
    if offer.amount != 0:
        return offer.price / offer.amount
    else:
        return 0


def find_most_profit_offer(offers):
    result_offer = list(offers)[0]
    for offer in list(offers)[1:]:
        if get_item_price(offer) < get_item_price(result_offer):
            result_offer = offer
    return result_offer


def is_offers_suitable(offer_b, offer_s):
    if offer_b.user != offer_s.user and \
            offer_b.item == offer_s.item and \
            get_item_price(offer_b) >= get_item_price(offer_s):
        return True
    else:
        return False

def make_trade(offer_b, offer_s):
    # Get trade amount & total price
    amount = offer_b.amount if offer_b.amount <= offer_s.amount else offer_s.amount
    total_price = amount * get_item_price(offer_s)

    # Making trade
    trade = Trade(item=offer_b.item, amount=amount, price=total_price, \
                  seller=offer_s.user, seller_offer=offer_s, buyer=offer_b.user, \
                  buyer_offer=offer_b)

    # Offers & inventories amount actions
    offer_b.amount -= amount;
    offer_s.amount -= amount;
    if Inventory.objects.filter(user=offer_b.user, item=offer_b.item).exists():
        inventory_b = get_object_or_404(Inventory, user=offer_b.user, item=offer_b.item)
    else:
        inventory_b = Inventory(user=offer_b.user, item=offer_b.item, amount=0)
        inventory_b.save()
    inventory_s = get_object_or_404(Inventory, user=offer_s.user, item=offer_s.item)
    inventory_s.amount -= amount
    inventory_b.amount += amount

    # Money actions
    money_action(offer_b.user, amount, "-")
    money_action(offer_s.user, amount, "+")

    # Check if offer is closed
    if offer_b.amount == 0:
        offer_b.is_active = False
    if offer_s.amount == 0:
        offer_s.is_active = False

    trade.save()
    offer_b.save()
    offer_s.save()
    inventory_b.save()
    inventory_s.save()


def find_suitable_offers(offer_b, offers):
    suitable_offers = []
    for offer_s in offers:
        if is_offers_suitable(offer_b, offer_s):
            suitable_offers.append(offer_s)
    if len(suitable_offers) != 0 and offer_b.is_active == True:
        profitable_offer = find_most_profit_offer(suitable_offers)
        make_trade(offer_b, profitable_offer)
        offers.pop(offers.index(profitable_offer))
        find_suitable_offers(offer_b, offers)


def offer_lists_creator(offers_list):
    offers_sell = [offer for offer in offers_list if (offer.type == 0 and offer.is_active == True)]
    offers_buy = [offer for offer in offers_list if (offer.type == 1 and offer.is_active == True)]
    return [offers_buy, offers_sell]


app.conf.beat_schedule = {
    'offer-selection-in-10-sec': {
        'task': 'api.tasks.offer_selection',
        'schedule': timedelta(seconds=60),
    },
}
