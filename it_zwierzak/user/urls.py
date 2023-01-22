from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('register/', views.register, name='register'),
]
