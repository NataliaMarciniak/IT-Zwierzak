from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Utworzono profil dla: ' + user)

            return redirect('homepage:login')

    context = {'form': form}
    return render(
        request,
        'homepage/register.html',
        context
    )


def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage:home')
        else:
            messages.info(request, 'Username lub password jest niepoprawne')

    context = {}
    return render(
        request,
        'homepage/login.html',
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
