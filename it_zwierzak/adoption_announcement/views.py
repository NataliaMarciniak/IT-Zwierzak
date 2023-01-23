from django.shortcuts import render
from django.views.generic import FormView
from .forms import AdoptionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



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


class AdoptionApplicationView(LoginRequiredMixin, FormView): #tylko dla zalogowanych
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

@login_required
def private_page(request):
    return render(request, 'adoption_announcement/adoption_application.html')
