from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email"
        ]


class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "website",
            "city",
            "signature"
        ]
