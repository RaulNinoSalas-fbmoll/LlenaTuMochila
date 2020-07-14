"""LlenaTuMochila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import include

from app.views import show_404, show_500

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^rest/', include('crm.urls')),
    url(r'^', include('app.urls')),
]
# if settings.DEBUG:
#     urlpatterns = [
#         url(r'404/$', show_404, name='show_404'),
#         url(r'500/$', show_500, name='show_500'),
#     ]