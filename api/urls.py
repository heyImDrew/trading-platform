from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from .views import CurrencyView, PriceView, ItemView, UserView, TradeView, \
    InventoryView, OfferView, WatchListView, MoneyView


router = routers.DefaultRouter()
router.register(r'currencies', CurrencyView, basename="Currencies")
router.register(r'prices', PriceView, basename="Prices")
router.register(r'items', ItemView, basename="Items")
router.register(r'reg', UserView, basename="Registration")
router.register(r'trades', TradeView, basename="Trades")
router.register(r'inventories', InventoryView, basename="Inventories")
router.register(r'offers', OfferView, basename="Offers")
router.register(r'watchlists', WatchListView, basename="WatchLists")
router.register(r'money', MoneyView, basename="Money")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('token/refresh/', refresh_jwt_token),
]