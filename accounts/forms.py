from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CreationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','name', 'email',)


class ChangeUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','name', 'email',)