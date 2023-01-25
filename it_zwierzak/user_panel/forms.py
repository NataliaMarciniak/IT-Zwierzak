from django.contrib.auth.models import User

from user import forms
from .models import Profile


class UserEditForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileEditForm(forms.UserCreationForm):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'address', 'phone', 'image', 'date_of_birth')