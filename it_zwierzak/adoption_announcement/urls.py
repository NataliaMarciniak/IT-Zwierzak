from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news', views.news, name='news'),
    path('adoptions', views.adoptions, name='adoptions'),
    path('adoption_card', views.adoption_card, name='adoption_card'),
    path('adoption_form', views.adoption_form, name='adoption_form')
]