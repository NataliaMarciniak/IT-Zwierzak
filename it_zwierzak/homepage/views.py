from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login(request):
    context = {}
    return render(
        request,
        'homepage/login.html',
        context
    )


def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(
        request,
        'homepage/register.html',
        context
    )


def homepage(request):
    return render(
        request,
        'homepage/home.html'
    )


def statute(request):
    return render(
        request,
        'homepage/statute.html'
    )


def contact(request):
    return render(
        request,
        'homepage/contact.html'
    )


def advice(request):
    return render(
        request,
        'homepage/advice.html'
    )
