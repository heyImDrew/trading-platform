from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404

from app.models import Money, WatchList


@receiver(post_save, sender=User)
def watchlist_autocreatiion(instance, **kwargs):
    watchlist = WatchList(user=get_object_or_404(User, username=instance))
    watchlist.save()

@receiver(post_save, sender=User)
def wallet_autocreation(instance, **kwargs):
    wallet_usd = Money(user=get_object_or_404(User, username=instance), money=0, currency_id=1)
    wallet_eur = Money(user=get_object_or_404(User, username=instance), money=0, currency_id=2)
    wallet_usd.save()
    wallet_eur.save()
