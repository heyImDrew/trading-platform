from datetime import timedelta

from trading_platform.celery import app
from app.models import Offer


@app.task
def offer_selection():
    print("~~~~~ TASK BEGINS:")
    offers = Offer.objects.all()
    offers_type_lists = offer_lists_creator(list(offers))
    offers_buy = offers_type_lists[0]
    offers_sell = offers_type_lists[1]
    for offer in offers_buy:
        find_suitable_offers(offer, offers_sell)


"""
When trade will come in, this methods will be used
"""


# def subtract_money(user, amount):
#     user.money = user.money - amount
#     user.save()
#
# def append_money(user, amount):
#     user.money = user.money + amount
#     user.save()


def get_item_price(offer):
    return offer.price / offer.amount


def find_most_profit_offer(offers):
    result_offer = list(offers)[0]
    for offer in list(offers)[1:]:
        if get_item_price(offer) < get_item_price(result_offer):
            result_offer = offer
    print(result_offer)


def is_offers_suitable(offer_b, offer_s):
    if offer_b.user != offer_s.user and \
    offer_b.item == offer_s.item and \
    get_item_price(offer_b) >= get_item_price(offer_s):
        return True
    else:
        return False


def find_suitable_offers(offer_b, offers):
    for offer_s in offers:
        if is_offers_suitable(offer_b, offer_s):
            print("~~~", "FIND SUITABLE OFFERS:", offer_b, offer_s, "~~~")


def offer_lists_creator(offers_list):
    offers_sell = [offer for offer in offers_list if (offer.type == 0 and offer.is_active == True)]
    offers_buy = [offer for offer in offers_list if (offer.type == 1 and offer.is_active == True)]
    return [offers_buy, offers_sell]


app.conf.beat_schedule = {
    'offer-selection-in-10-sec': {
        'task': 'api.tasks.offer_selection',
        'schedule': timedelta(seconds=10),
    },
}