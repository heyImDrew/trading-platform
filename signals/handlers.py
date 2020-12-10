from django.db.models.signals import post_save, pre_save
from django.core.signals import request_finished, request_started
from django.dispatch import receiver

from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404

from app.models import Money, WatchList


@receiver(post_save, sender=User)
def watchlist_autocreatiion(instance, **kwargs):
    if not (WatchList.objects.filter(user=get_object_or_404(User, username=instance)).exists()):
        watchlist = WatchList(user=get_object_or_404(User, username=instance))
        watchlist.save()
        print("WatchList created!")


@receiver(post_save, sender=User)
def wallet_autocreation(instance, **kwargs):
    if not (Money.objects.filter(user=get_object_or_404(User, username=instance))):
        wallet_usd = Money(user=get_object_or_404(User, username=instance), money=0, currency_id=1)
        wallet_eur = Money(user=get_object_or_404(User, username=instance), money=0, currency_id=2)
        wallet_usd.save()
        wallet_eur.save()
        print("Wallets created!")


@receiver(pre_save, sender=User)
def presave_user_printout(instance, **kwargs):
    print("Trying to create User...")


@receiver(post_save, sender=User)
def postsave_user_printout(instance, **kwargs):
    print("User created!")


@receiver(request_started)
def request_start_callback(sender, **kwargs):
    print("Request started")


@receiver(request_finished)
def request_finished_callback(sender, **kwargs):
    print("Request finished")