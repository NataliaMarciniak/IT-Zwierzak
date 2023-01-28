from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView, DetailView
from .forms import AdoptionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal, Announcement


def adopted(request):
    return render(request, 'adoption_announcement/adopted_animals.html')


class AnnouncementView(ListView):
    model = Animal
    template_name = 'adoption_announcement/test_announcements.html'


class AnnouncementDetailView(DetailView):
    model = Animal
    template_name = 'adoption_announcement/test_details.html'



def announcement(request):
    announcement_data = Announcement.objects.all()
    return render(request, 'adoption_announcement/animals_for_adoption.html', {'announcement_data': announcement_data})


def adoption_card(request):
    return render(request, 'adoption_announcement/announcement_detail.html')


def adoption_form(request):
    return render(request, 'adoption_announcement/adoption_application.html')


def confirmation_adoption_application(request):
    return render(request, 'confirmation_adoption_application.html')


class AdoptionApplicationView(LoginRequiredMixin, FormView):
    template_name = 'adoption_announcement/adoption_application.html'

    def get(self, request):
        form = AdoptionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AdoptionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            form = AdoptionForm()
            return redirect('confirmation_adoption_application:confirmation_adoption_application')
            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)



