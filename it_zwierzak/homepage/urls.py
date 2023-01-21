from django.urls import path
from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('statute/', views.statute, name='statute'),
    path('contact/', views.contact, name='contact'),
    path('advice/', views.advice, name='advice'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]