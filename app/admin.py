from django.contrib import admin
from .models import (
    Currency,
    Item,
    Price,
    WatchList,
    Offer,
    Trade,
    Inventory,
    Money
)

admin.site.register(Currency)
admin.site.register(Item)
admin.site.register(Price)
admin.site.register(WatchList)
admin.site.register(Offer)
admin.site.register(Trade)
admin.site.register(Inventory)
admin.site.register(Money)