from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.Form):
    username = forms.CharField(label="Nazwa użytkownika")
    first_name = forms.CharField(label="Imię")
    last_name = forms.CharField(label="Nazwisko")
    email = forms.EmailField(label="Email")
    date_of_birth = forms.DateField(
        label="Data urodzenia",
        widget=forms.widgets.DateInput(
            attrs={"type": "date"}))
    phone_number = forms.IntegerField(label="Numer telefonu")
    street = forms.CharField(label="Ulica")
    house_number = forms.IntegerField(label="Numer domu")
    apartment_number = forms.IntegerField(label="Numer mieszkania")
    postcode = forms.IntegerField(label="Kod pocztowy")
    city = forms.CharField(label="Miasto")


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
