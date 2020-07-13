from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.

class CountryAPIView(generics.ListCreateAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer


class CambioEurAPIView(generics.ListCreateAPIView):
    queryset = cambioEur.objects.all()
    serializer_class = CambioEurSerializer


class CambioUsdAPIView(generics.ListCreateAPIView):
    queryset = cambioUsd.objects.all()
    serializer_class = CambioUsdSerializer


class UsersAPIView(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = UsersSerializer