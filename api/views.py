from rest_framework.response import Response
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth.models import User
from app.models import Currency, Price, Item
from .serializers import CurrencySerializer, PriceSerializer, ItemSerializer, UserSerializer


class UserView (
    viewsets.GenericViewSet,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.UpdateModelMixin,
    ):
    permission_classes = [AllowAny,]
    """
    User view.
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
        

class CurrencyView (
    viewsets.GenericViewSet,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin,
    ):
    """
    Currency view.
    """
    queryset = Currency.objects.all()
    default_serializer_class = CurrencySerializer
    serializer_classes =  {
        "list": CurrencySerializer,
        "retrieve": CurrencySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class PriceView (
    viewsets.GenericViewSet,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin
    ):
    """
    Price view.
    """
    queryset = Price.objects.all()
    default_serializer_class = PriceSerializer
    serializer_classes = {
        "list": PriceSerializer,
        "retrieve": PriceSerializer,
        "update": PriceSerializer,
        "create": PriceSerializer,
    }


class ItemView (
    viewsets.GenericViewSet,
    mixins.ListModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    ):
    """
    Item view.
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