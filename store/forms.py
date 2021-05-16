from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True , help_text='Required.')

    class Meta:
        model = User
        fields = ('first_name','last_name' , 'email','username' , 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)


class ProfileForm(forms.ModelForm):
    address = forms.CharField(max_length=200, required=True, help_text='Required.')
    city = forms.CharField(max_length=50, required=True, help_text='Required.')
    country = forms.CharField(max_length=30, required=True, help_text='Required.')
    zipcode = forms.CharField(max_length=5, required=True, help_text='Required.')
    phone = forms.CharField(max_length=10, required=True, help_text='Required.')
    class Meta:
        model = Profile
        fields = ('address','city','country','zipcode','phone')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('address','city','country','zipcode','phone')

class AddressFrom(forms.ModelForm):
    name = forms.CharField(max_length=200, required=True, help_text='Required.')
    address = forms.CharField(max_length=200, required=True, help_text='Required.')
    city = forms.CharField(max_length=50, required=True, help_text='Required.')
    country = forms.CharField(max_length=30, required=True, help_text='Required.')
    zipcode = forms.CharField(max_length=5, required=True, help_text='Required.')
    class Meta:
        model = Profile
        fields = ('name','address','city','country','zipcode','phone')






