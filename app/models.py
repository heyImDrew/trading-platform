from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    code = models.CharField(max_length=255, unique=True, blank=False)
    currency = models.ForeignKey("Currency", on_delete=models.CASCADE, blank=False)

class Price(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)