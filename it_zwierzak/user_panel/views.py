from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditUserForm, EditUserProfileForm

