from rest_framework import serializers

from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = "__all__"


class CambioEurSerializer(serializers.ModelSerializer):
    class Meta:
        model = cambioEur
        fields = "__all__"


class CambioUsdSerializer(serializers.ModelSerializer):
    class Meta:
        model = cambioUsd
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"
