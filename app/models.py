from django.db import models


class Currency (
    models.Model
    ):
    """
    Currency model.
    """
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return self.name


class Item (
    models.Model
    ):
    """
    Item model.
    """
    name = models.CharField(max_length=255, unique=True, blank=False)
    code = models.CharField(max_length=255, unique=True, blank=False)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.code


class Price (
    models.Model
    ):
    """
    Price model.
    """
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    item = models.OneToOneField("Item", on_delete=models.CASCADE)

    def __str__(self):
        return self.item.code + " " + str(self.price) + " " + self.item.currency.name
