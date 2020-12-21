from datetime import timedelta

from rest_framework.generics import get_object_or_404

from trading_platform.celery import app
from app.models import Offer, Trade, Money, Inventory
from api.TradeServices import (
    offer_lists_creator,
    find_most_suitable_offer,
    find_suitable_offers,
    make_trade,
    is_offer_suitable,
    get_item_price,
    money_action,
)

@app.task
def offer_selection():
    offers = list(Offer.objects.select_related('item'))
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