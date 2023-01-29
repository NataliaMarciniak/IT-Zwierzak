from django.urls import path
from .views import AdoptionApplicationView, Announcement, AnimalDetail
from . import views

urlpatterns = [
    path('adopted_animals', views.adopted, name='adopted_animals'),
    path('animals_for_adoption', Announcement.as_view(), name='animals_for_adoption'),
    path('article/<int:pk>', AnimalDetail.as_view(), name='animal_detail'),
    path('adoption_form/<int:pk>', AdoptionApplicationView.as_view(), name='adoption_application'),
    path('confirmation_adoption_application', views.confirmation_adoption_application,
         name='confirmation_adoption_application'),
]
