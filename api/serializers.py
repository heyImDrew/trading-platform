from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import Currency, Price, Item, WatchList, Offer, Inventory, Trade, Money


class UserSerializer(
    serializers.ModelSerializer
):
    """
    Serializer for User
    """

    class Meta:
        model = User
        fields = ['username', 'password', ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CurrencySerializer(
    serializers.ModelSerializer
):
    """
    Serializer for Currency
    """

    class Meta:
        model = Currency
        fields = "__all__"


class PriceSerializer(
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


class WatchListSerializer(
    serializers.ModelSerializer
):
    """
    Serializer for WatchList
    """

    class Meta:
        model = WatchList
        fields = "__all__"


class OfferSerializer(
    serializers.ModelSerializer
):
    """
    Serializer for Offer
    """

    def validate(self, data):
        if data['type'] == 0 and data['amount'] > \
                get_object_or_404(Inventory, user_id=data['user'], item_id=data['item']).amount:
            raise serializers.ValidationError("Amount of sell should be less or equals then user have in inventory.")
        if data['type'] == 1 and data['price'] > \
                get_object_or_404(Money, user_id=data['user']).money:
            raise serializers.ValidationError("Price should be less or equals then user have in inventory.")
        data['is_active'] = True
        return data

    class Meta:
        model = Offer
        fields = "__all__"


class InventorySerializer(
    serializers.ModelSerializer
):
    """
    Serializer for Inventory
    """

    class Meta:
        model = Inventory
        fields = "__all__"


class TradeSerializer(
    serializers.ModelSerializer
):
    """
    Serializer for Trade
    """

    class Meta:
        model = Trade
        fields = "__all__"


class MoneySerializer(
    serializers.ModelSerializer
):
    """
    Serializer for Money
    """

    class Meta:
        model = Money
        fields = "__all__"
