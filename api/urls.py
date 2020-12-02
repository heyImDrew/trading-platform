from django.urls import path, include
from rest_framework import routers
from .views import CurrencyViewSet, PriceViewSet, ItemViewSet, UserView

router = routers.DefaultRouter()
router.register(r'currencies', CurrencyViewSet, basename="Currencies")
router.register(r'prices', PriceViewSet, basename="Prices")
router.register(r'items', ItemViewSet, basename="Items")
router.register(r'reg', UserView, basename="reg")

urlpatterns = [
    path('', include(router.urls)),
]