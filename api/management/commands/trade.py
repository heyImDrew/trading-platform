from django.core.management.base import BaseCommand, CommandError
from api.tasks import make_trade, is_offer_suitable, find_most_suitable_offer
from app.models import Offer


class Command(BaseCommand):
    help = 'Autotrade for exact user'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs=1, type=int)

    def handle(self, *args, **options):
        user_id = options['id'][0]
        offers_b_iter = iter(Offer.objects.filter(user_id=user_id, type=1, is_active=True))
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
