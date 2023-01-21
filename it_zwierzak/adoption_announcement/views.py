from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .templates import forms

def index(request):
    return HttpResponse("Ogłoszenie Adopcji")

def base(request):
    return render(request, 'adoption_announcement/base.html')

def adopted(request):
    return render(request, 'adoption_announcement/adopted.html')

def adoptions(request):
    return render(request, 'adoption_announcement/adoptions.html')

def adoption_card(request):
    return render(request, 'adoption_announcement/adoption_card.html')

def adoption_form(request):
    return render(request, 'adoption_announcement/adoption_form.html')
