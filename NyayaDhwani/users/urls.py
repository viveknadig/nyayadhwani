from django.urls import path,re_path
from .views import home, profile, RegisterView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    re_path(r"^profile/$", profile, name='users-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
