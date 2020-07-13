from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout as django_logout, login as django_login, authenticate

# Create your views here.


def main(request):
    context = {}
    return render(request, 'tumochila/block/home.html', context)


def login(request):
    context = {}

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('TuMochilaApp:login'))

    if request.POST:
        django_logout(request)
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            django_login(request, user)
            return HttpResponseRedirect(reverse('TuMochilaApp:main'))

    return render(request, 'tumochila/block/login.html', context)


def register(request):
    context = {}
    if request.method == "POST":
        try:
            user = User.objects.create(
                email=request.POST['email'],
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                is_active=True,
            )

            user.set_password(request.POST['password'])
            user.save()
            django_login(request, user)

            return HttpResponseRedirect(reverse('TuMochilaApp:login'))

        except IntegrityError:
            pass

    return render(request, 'tumochila/block/register.html', context)

