from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from app.models import Currency, Price, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password',]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
