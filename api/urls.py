from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from .views import CurrencyView, PriceView, ItemView, UserView


router = routers.DefaultRouter()
router.register(r'currencies', CurrencyView, basename="Currencies")
router.register(r'prices', PriceView, basename="Prices")
router.register(r'items', ItemView, basename="Items")
router.register(r'reg', UserView, basename="reg")

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('token/refresh/', refresh_jwt_token),
]