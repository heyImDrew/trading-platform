from enum import Enum

from django.db import models
from django.contrib.auth.models import User


class Currency(
    models.Model
):
    """
    Currencies for stock pricing
    """
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class Item(
    models.Model
):
    """
    Stock
    """
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    code = models.CharField(max_length=255, unique=True, blank=False, null=False)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=False, null=False,
                                 related_name="item_currency")

    def __str__(self):
        return self.code


class Price(
    models.Model
):
    """
    Price of stock
    """
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    item = models.OneToOneField("Item", on_delete=models.CASCADE, related_name="item_price")

    def __str__(self):
        return self.item.code + " " + str(self.price) + " " + self.item.currency.name


class WatchList(
    models.Model
):
    """
    Favourite list of stocks for current user
    """
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE, related_name="watchlist_user")
    items = models.ManyToManyField("Item", blank=True, related_name="watchlist_items")

    def __str__(self):
        return self.user.username + "'s watchlist"


class OfferType(Enum):
    SELL = "SELL"
    BUY = "BUY"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Offer(
    models.Model
):
    """
    User offer to buy certain amount of stocks for certain price
    """

    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="offer_user")
    item = models.ForeignKey("Item", null=False, blank=False, on_delete=models.CASCADE, related_name="offer_item")
    amount = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    type = models.CharField(choices=OfferType.choices(), max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.type) + " | " + self.item.code + (
            " offer by ") + self.user.username + ": " + str(self.amount) + " for " + str(
            self.price) + " " + self.item.currency.name + " | IS_ACTIVE:" + str(self.is_active)


class Trade(
    models.Model
):
    """
    Trading sell and buy offers
    """
    item = models.ForeignKey("Item", null=True, blank=False, on_delete=models.CASCADE, related_name="trade_item")
    amount = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    seller = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="seller")
    seller_offer = models.ForeignKey("Offer", blank=False, null=False, on_delete=models.CASCADE,
                                     related_name="seller_offer")
    buyer = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="buyer")
    buyer_offer = models.ForeignKey("Offer", blank=False, null=False, on_delete=models.CASCADE,
                                    related_name="buyer_offer")

    def __str__(self):
        return self.seller.username + " & " + self.buyer.username + " offer: " + str(
            self.amount) + self.item.name + " for " + str(self.price)


class Inventory(
    models.Model
):
    """
    Current user stock amount
    """
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="inventory_user")
    item = models.ForeignKey("Item", null=False, blank=False, on_delete=models.CASCADE, related_name="inventory_item")
    amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.user.username + ": " + str(self.amount) + " of " + self.item.name


class Money(
    models.Model
):
    """
    Amount of user's money
    """
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="money_user")
    money = models.IntegerField(blank=False, null=False)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=False, null=False,
                                 related_name="money_currency")

    def __str__(self):
        return self.user.username + ": " + str(self.money) + " " + self.currency.name
