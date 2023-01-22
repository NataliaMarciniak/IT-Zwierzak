from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from .forms import AdoptionForm
from .models import AdoptionApplication


# zaadoptowane
def adopted(request):
    return render(request, 'adoption_announcement/adopted_animals.html')


# przeniesienie do strony z kafelkami adopcji
def adoptions(request):
    return render(request, 'adoption_announcement/animals_to_adoption.html')


# przeniesienie do konkretnego ogłoszenia zwierzęcia, po id z bazy danych
def adoption_card(request):
    return render(request, 'adoption_announcement/announcement_detail.html')


def adoption_form(request):
    return render(request, 'adoption_announcement/adoption_application.html')


class AdoptionApplicationView(FormView):
    template_name = 'adoption_announcement/adoption_application.html'
    form_class = AdoptionForm
    success_url = '/animals_to_adoption'


def adoption_application_view(request):
    form = AdoptionForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'adoption_announcement/adoption_application.html', context)
