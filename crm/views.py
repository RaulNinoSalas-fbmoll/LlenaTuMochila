from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class CountryAPIView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CambioEurAPIView(generics.ListCreateAPIView):
    queryset = CambioEuro.objects.all()
    serializer_class = CambioEurSerializer


class CambioUsdAPIView(generics.ListCreateAPIView):
    queryset = CambioDolar.objects.all()
    serializer_class = CambioUsdSerializer


class UsersAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer


class InfoAPIView(generics.ListCreateAPIView):
    queryset = Info_country.objects.all()
    serializer_class = InfoSerializer
