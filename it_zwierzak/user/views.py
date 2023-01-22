from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utworzono profil dla: {username}')

            return redirect('user:login')

    context = {'form': form}
    return render(
        request,
        'user/register.html',
        context
    )


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage:home')
        else:
            messages.info(request, 'Nazwa użytkownika lub hasło jest niepoprawne')

    return render(
        request,
        'user/login.html',
    )


