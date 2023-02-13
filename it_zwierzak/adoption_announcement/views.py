from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .forms import AdoptionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal


def adopted(request):
    return render(request, 'adoption_announcement/adopted_animals.html')


class Announcement(ListView):
    model = Animal
    template_name = 'adoption_announcement/animals_for_adoption.html'


class AnimalDetail(DetailView):
    model = Animal
    template_name = 'adoption_announcement/announcement_detail.html'


def adoption_form(request):
    return render(request, 'adoption_announcement/adoption_application.html')


def confirmation_adoption_application(request):
    return render(request, 'confirmation_adoption_application.html')


class AdoptionApplicationView(View):
    model = Animal
    template_name = 'adoption_announcement/adoption_application.html'
    template_confirm = 'adoption_announcement/confirmation_adoption_application.html'

    def get(self, request, pk):
        form = AdoptionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        form = AdoptionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            form = AdoptionForm()
            args = {'form': form, 'text': text}
            return render(request, self.template_confirm, args)

