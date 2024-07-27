from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Lawyers,Clients

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.NumberInput()
    class Meta:
        model = Lawyers
        fields = ['username', 'email','password1', 'password2','phone_number']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Clients
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
