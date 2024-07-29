from django.urls import path,include
from re import template
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_views
from users import views
app_name = 'dashboard'

urlpatterns = [
    path('clients',dashboard_views.clients,name='clients'),
    path('lawyers',dashboard_views.lawyers,name='lawyers'),
    path('register',dashboard_views.reg,name='register_case'),
    path('activeclientcase',dashboard_views.active_client_list,name='active-case-list'),
    path('totalclientcase',dashboard_views.total_client_list,name='total-case-list'),
    path('wonclientcase',dashboard_views.won_client_list,name='won-case-list'),
    path('lossclientcase',dashboard_views.loss_client_list,name='loss-case-list'),
]