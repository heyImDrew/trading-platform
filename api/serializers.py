from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from app.models import Currency, Price, Item


class UserSerializer (
    serializers.ModelSerializer
    ):
    """
    Serializer for User
    """
    class Meta:
        model = User
        fields = ['username', 'password',]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CurrencySerializer (
    serializers.ModelSerializer
    ):
    """
    Serializer for Currency
    """
    class Meta:
        model = Currency
        fields = "__all__"


class PriceSerializer (
    serializers.ModelSerializer
    ):
    """
    Serializer for Price
    """
    class Meta:
        model = Price
        fields = "__all__"


class ItemSerializer(
    serializers.ModelSerializer
    ):
    """
    Serializer for Item
    """
    class Meta:
        model = Item
        fields = "__all__"