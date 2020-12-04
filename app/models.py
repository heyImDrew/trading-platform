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
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.code


class Price(
    models.Model
):
    """
    Price of stock
    """
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    item = models.OneToOneField("Item", on_delete=models.CASCADE)

    def __str__(self):
        return self.item.code + " " + str(self.price) + " " + self.item.currency.name


class WatchList(
    models.Model
):
    """
    Favourite list of stocks for current user
    """
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    items = models.ManyToManyField("Item", blank=True)

    def __str__(self):
        return self.user.username + "'s watchlist"


class Offer(
    models.Model
):
    """
    User offer to buy certain amount of stocks for certain price
    """
    ORDER_TYPE_CHOICES = (
        (0, "Sell"),
        (1, "Buy"),
    )

    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", null=False, blank=False, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    type = models.IntegerField(choices=ORDER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ORDER_TYPE_CHOICES[self.type][1]) + " | " + self.item.code + \
               " offer by " + self.user.username + ": " + str(self.amount) + " for " + str(self.price) + \
               " " + self.item.currency.name + " | IS_ACTIVE:" + str(self.is_active)


class Trade(
    models.Model
):
    """
    Trading sell and buy offers
    """
    item = models.ForeignKey("Item", null=True, blank=False, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", null=False, blank=False, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.user.username + ": " + str(self.amount) + " of " + self.item.name


class Money(
    models.Model
):
    """
    Amount of user's money
    """
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    money = models.IntegerField(blank=False, null=False)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.user.username + ": " + str(self.money) + " " + self.currency.name
