from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app import views
from app.views import show_404, show_500

app_name = 'app'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^information/$', views.information, name='information'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^profile/$',views.profile, name='profile'),

    # url(r'recover-password/$', views.recover_password, name='recover_password'),
]

