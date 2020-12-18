from django.contrib import admin
from .models import (
    Currency,
    Item,
    WatchList,
    Offer,
    Trade,
    Inventory,
    Money
)


class CurrencyAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class ItemAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code',)
    list_display = ('name', 'code',)


class WatchListAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)


class OfferAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'item__code', 'type',)


class TradeAdmin(admin.ModelAdmin):
    search_fields = ('item__name', 'price', 'seller__username', 'buyer__username',)


class InventoryAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'item__code')


class MoneyAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'currency__name',)
    list_display = ('user', 'currency',)


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Money, MoneyAdmin)
