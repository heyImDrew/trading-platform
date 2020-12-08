from django.core.management.base import BaseCommand, CommandError
from api.tasks import make_trade, is_offer_suitable, find_most_suitable_offer
from app.models import Offer


class Command(BaseCommand):
    help = 'Autotrade for exact user'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs=1, type=int)

    def handle(self, *args, **options):
        id = options['id'][0]

        offers_b = Offer.objects.filter(user_id=id, type=1, is_active=True)
        offers_s = Offer.objects.filter(type=0, is_active=True)
        for offer_b in offers_b:
            suitable_offers = []
            for offer_s in offers_s:
                if is_offer_suitable(offer_b, offer_s):
                    suitable_offers.append(offer_s)
            most_suitable = find_most_suitable_offer(suitable_offers)
            make_trade(offer_b, most_suitable)
