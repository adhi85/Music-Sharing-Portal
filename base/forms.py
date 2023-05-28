from django import forms
from . models import Musics, User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class MusicForm(forms.ModelForm):
    class Meta:
        model = Musics
        fields = '__all__'
        exclude = ['uploaded_by',]

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
