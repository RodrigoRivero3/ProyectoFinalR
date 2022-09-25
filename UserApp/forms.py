from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User

from UserApp.models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('user', 'imagen')