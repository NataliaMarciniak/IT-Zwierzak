from django.urls import path
from .views import AdoptionApplicationView
from . import views

urlpatterns = [
    path('adopted_animals', views.adopted, name='adopted_animals'),
    path('animals_for_adoption', views.announcement, name='animals_for_adoption'),
    path('announcement_detail', views.adoption_card, name='announcement_detail'),
    path('adoption_application', AdoptionApplicationView.as_view(), name='adoption_application'),
    path('confirmation_adoption_application', views.confirmation_adoption_application,
         name='confirmation_adoption_application'),
]
