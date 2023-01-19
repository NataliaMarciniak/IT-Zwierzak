from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ogłoszenie Adopcji")

def base(request):
    return render(request, 'adoption_announcement/base.html')

def home_page(request):
    return render(request, 'adoption_announcement/home_page.html')

def news(request):
    return render(request, 'adoption_announcement/news.html')

def adoptions(request):
    return render(request, 'adoption_announcement/adoptions.html')

def adoption_card(request):
    return render(request, 'adoption_announcement/adoption_card.html')

def adoption_form(request):
    return render(request, 'adoption_announcement/adoption_form.html')