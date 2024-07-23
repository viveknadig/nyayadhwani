from django.urls import path,include
from re import template
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import (ClientsListView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView,
                         LawyersListView, LawyersCreateView, LawyersUpdateView, LawyersDeleteView)

app_name = 'users'

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    path('clients', ClientsListView.as_view(), name='clients-list'),
    path('clients/new/', ClientsCreateView.as_view(), name='clients-create'),
    path('clients/<int:pk>/update/', ClientsUpdateView.as_view(), name='clients-update'),
    path('clients/<int:pk>/delete/', ClientsDeleteView.as_view(), name='clients-delete'),
    path('lawyers', LawyersListView.as_view(), name='lawyers-list'),
    path('lawyers/new/', LawyersCreateView.as_view(), name='lawyers-create'),
    path('lawyers/<int:pk>/update/', LawyersUpdateView.as_view(), name='lawyers-update'),
    path('lawyers/<int:pk>/delete/', LawyersDeleteView.as_view(), name='lawyers-delete'),
    path('dashboard',user_views.dashboard,name='dashboard'),
]