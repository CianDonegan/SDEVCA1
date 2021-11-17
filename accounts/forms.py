from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
            model = CustomUser
            fields = ('username', 'email', 'age',)


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','platform','bio')