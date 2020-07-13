from django.conf.urls import url
from . import views

app_name = 'MochilaApp'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^profile/$',views.profile, name='profile'),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'recover-password/$', views.recover_password, name='recover_password'),
]