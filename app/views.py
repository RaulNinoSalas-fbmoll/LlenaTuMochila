
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from crm.forms import userForm
from crm.models import CustomUser, Country, CambioDolar, CambioEuro, Info_country


# Create your views here.


# def show_404(request):
#     return render(request, '404.html', {})
#
#
# def show_500(request):
#     return render(request, '500.html', {})


def main(request):
    countries = Country.objects.all()
    return render(request, 'app/block/home.html', {'countries': countries})


def information(request):
    countries = Country.objects.all()
    country_id = request.POST['country']
    country = Country.objects.get(pk=country_id)
    info_country = Info_country.objects.filter(country_id=country_id).first()
    cambioDolar = CambioDolar.objects.all()
    cambioEuro = CambioEuro.objects.all()
    return render(request, 'app/block/country.html', {'countries': countries, 'cambioEuro': cambioEuro, 'cambioDolar': cambioDolar, 'info_country':info_country, 'country': country})


def logout(request, CustomUser):
    if request.user:
        django_logout(request)
    return HttpResponseRedirect(reverse('app:main'))


def login(request):
    context = {}

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:main'))

    if request.POST:
        django_logout(request)
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            django_login(request, user)
            return HttpResponseRedirect(reverse('app:main'))

    return render(request, 'app/block/login.html', context)


def register(request):
    form = userForm()

    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            django_login(new_user)
            return HttpResponseRedirect(reverse('app:main'))

    return render(request, 'app/block/register.html', {'form': userForm})


def show_404(request):
    return render(request, '404.html', {})


def show_500(request):
    return render(request, '500.html', {})