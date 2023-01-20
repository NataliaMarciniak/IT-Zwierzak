from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

def login(request):
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('user_panel:index'))

def logout(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('user_panel:index'))
