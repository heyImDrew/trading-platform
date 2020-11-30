from django.contrib import admin
from .models import Currency, Item, Price

admin.site.register(Currency)
admin.site.register(Item)
admin.site.register(Price)