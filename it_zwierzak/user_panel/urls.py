from django.urls import path
from . import views

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('rejestruj', CreateView.as_view(
        template_name='user_panel/register.html',
        form_class=UserCreationForm)),
    path('loguj', views.login, name='loguj'),
    path('wyloguj', views.logout, name='wyloguj'),

]




