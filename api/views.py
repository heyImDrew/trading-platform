from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth.models import User
from app.models import (
    Currency,
    Price,
    Item,
    WatchList,
    Trade,
    Offer,
    Inventory,
    Money
)
from .serializers import (
    CurrencySerializer,
    PriceSerializer,
    ItemSerializer,
    UserSerializer,
    WatchListSerializer,
    TradeSerializer,
    OfferSerializer,
    InventorySerializer,
    MoneySerializer
)


class UserView(
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.UpdateModelMixin,
):
    permission_classes = [AllowAny, ]
    """
    User view
    """
    queryset = User.objects.all()
    default_serializer_class = UserSerializer
    serializer_classes = {
        "create": UserSerializer,
        "list": UserSerializer,
        "retrieve": UserSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CurrencyView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    """
    Currency view
    """
    queryset = Currency.objects.all()
    default_serializer_class = CurrencySerializer
    serializer_classes = {
        "list": CurrencySerializer,
        "retrieve": CurrencySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class PriceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin
):
    """
    Price view
    """
    queryset = Price.objects.all()
    default_serializer_class = PriceSerializer
    serializer_classes = {
        "list": PriceSerializer,
        "retrieve": PriceSerializer,
        "update": PriceSerializer,
        "create": PriceSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class ItemView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    """
    Item view
    """
    queryset = Item.objects.all()
    default_serializer_class = ItemSerializer
    serializer_classes = {
        "list": ItemSerializer,
        "retrieve": ItemSerializer,
        "create": ItemSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class WatchListView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    """
    WatchList view
    """
    queryset = WatchList.objects.all()
    default_serializer_class = WatchListSerializer
    serializer_classes = {
        "list": WatchListSerializer,
        "retrieve": WatchListSerializer,
        "update": WatchListSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class TradeView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    """
    Trade view
    """
    queryset = Trade.objects.all()
    default_serializer_class = TradeSerializer
    serializers_classes = {
        "list": TradeSerializer,
        "retrieve": TradeSerializer,
        "create": TradeSerializer,
    }

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)


class OfferView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    """
    Offer view
    """
    queryset = Offer.objects.all()
    default_serializer_class = OfferSerializer
    serializers_classes = {
        "list": OfferSerializer,
        "retrieve": OfferSerializer,
        "create": OfferSerializer,
    }

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)


class InventoryView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    """
    Inventory view
    """
    queryset = Inventory.objects.all()
    default_serializer_class = InventorySerializer
    serializers_classes = {
        "list": InventorySerializer,
        "retrieve": InventorySerializer,
        "create": InventorySerializer,
        "update": InventorySerializer,
    }

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)


class MoneyView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    """
    Money view
    """
    queryset = Money.objects.all()
    default_serializer_class = MoneySerializer
    serializers_classes = {
        "list": MoneySerializer,
        "retrieve": MoneySerializer,
        "update": MoneySerializer,
    }

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.default_serializer_class)
