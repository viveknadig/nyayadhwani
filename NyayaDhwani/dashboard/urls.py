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
    path('register',dashboard_views.register_case,name='register_case'),
    path('activeclientcase',dashboard_views.active_client_list,name='active-client-list'),
    path('totalclientcase',dashboard_views.total_client_list,name='total-client-list'),
    path('wonclientcase',dashboard_views.won_client_list,name='won-client-list'),
    path('lossclientcase',dashboard_views.loss_client_list,name='loss-client-list'),
    path('activelawyercase',dashboard_views.active_lawyer_list,name='active-lawyer-list'),
    path('totallawyercase',dashboard_views.total_lawyer_list,name='total-lawyer-list'),
    path('wonlawyercase',dashboard_views.won_lawyer_list,name='won-lawyer-list'),
    path('losslawyercase',dashboard_views.loss_lawyer_list,name='loss-lawyer-list'),
    path('case/view/<int:pk>',dashboard_views.case_view_check,name='case-view'),
    path('case/edit/<int:pk>',dashboard_views.update_case,name='case-edit'),
]