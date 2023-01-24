from django.shortcuts import render
from django.views.generic import FormView
from .forms import AdoptionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Announcement


def adopted(request):
    return render(request, 'adoption_announcement/adopted_animals.html')


def adoptions(request):
    data = Announcement.objects.all()
    return render(request, 'adoption_announcement/animals_for_adoption.html', {'data': data})

# def index(request):
#     data = Announcement.objects.all()
#     return render(request, 'adoption_announcement/animals_for_adoption.html', {'data': data})


def adoption_card(request):
    return render(request, 'adoption_announcement/announcement_detail.html')


def adoption_form(request):
    return render(request, 'adoption_announcement/adoption_application.html')


class AdoptionApplicationView(LoginRequiredMixin, FormView):
    template_name = 'adoption_announcement/adoption_application.html'
    form_class = AdoptionForm
    success_url = '/animals_for_adoption'


def adoption_application_view(request):
    form = AdoptionForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'adoption_announcement/adoption_application.html', context)

# @login_required
# def adopted_application_for_logged_in(request):
#     return render(request, 'adoption_announcement/adoption_application.html')

