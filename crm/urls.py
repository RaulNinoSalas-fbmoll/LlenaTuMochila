
from django.conf.urls import url
from crm import views

app_name = 'crm'

urlpatterns = [

    url(r'^$', views.CountryAPIView.as_view(), name='countrieslist'),
    url(r'^cambioeur/$', views.CambioEurAPIView.as_view(), name='cambioEur'),
    url(r'^cambiousd/$', views.CambioUsdAPIView.as_view(), name='cambioUsd'),
    url(r'^users/$', views.UsersAPIView.as_view(), name='users_list'),
    url(r'^info/$', views.InfoAPIView.as_view(), name='info_list'),
]
