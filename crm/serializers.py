from rest_framework import serializers

from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CambioEurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioEuro
        fields = "__all__"


class CambioUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioDolar
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'nickname', 'email', 'country']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info_country
        fields = "__all__"
