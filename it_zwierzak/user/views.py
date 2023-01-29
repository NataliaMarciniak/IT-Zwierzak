from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import Profile
from .forms import CreateUserForm, ProfileForm, ChangePasswordForm


def register(request):
    if request.user.is_authenticated:
        return redirect('homepage:home')
    else:
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


def login(request):
    if request.user.is_authenticated:
        return redirect('homepage:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('homepage:home')
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło jest niepoprawne')

        return render(
            request,
            'user/login.html',
        )


def logout(request):
    auth_logout(request)
    return redirect('user:login')


@login_required(login_url='login')
def profile(request):

    if request.method == "GET":
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            form = ProfileForm(initial={
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'date_of_birth': profile.date_of_birth,
                'phone_number': profile.phone_number,
                'street': profile.street,
                'house_number': profile.house_number,
                'apartment_number': profile.apartment_number,
                'postcode': profile.postcode,
                'city': profile.city
            })
        except Profile.DoesNotExist:
            form = ProfileForm(initial={
                'username': user.username
            })
        return render(request, 'user/user_profile.html', {'form': form})

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            data = form.cleaned_data
            try:
                profile = Profile.objects.get(user=user)
                user.first_name = data.get('first_name')
                user.last_name = data.get('last_name')
                user.email = data.get('email')
                profile.date_of_birth = data.get('date_of_birth')
                profile.phone_number = data.get('phone_number')
                profile.street = data.get('street')
                profile.house_number = data.get('house_number')
                profile.apartment_number = data.get('apartment_number')
                profile.postcode = data.get('postcode')
                profile.city = data.get('city')
                profile.save()
                user.save()

            except Profile.DoesNotExist:
                Profile.objects.create(
                    user=user,
                    date_of_birth=data.get('date_of_birth'),
                    phone_number=data.get('phone_number'),
                    street=data.get('street'),
                    house_number=data.get('house_number'),
                    apartment_number=data.get('apartment_number'),
                    postcode=data.get('postcode'),
                    city=data.get('city'),
                )

        return redirect('user:confirmation_message')

    form = ProfileForm()
    return render(request, 'user/user_profile.html', {'form': form})


@login_required(login_url='login')
def confirmation(request):
    return render(request, 'user/confirmation_message.html')


@login_required(login_url='login')
def change(request):
    form = ChangePasswordForm

    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Twoje hasło zostało pomyślnie zaktualizowane')
            return redirect('user:change_password')
        else:
            messages.error(request, 'Proszę popraw poniższy błąd')

    context = {'form': form}
    return render(
        request,
        'user/change_password.html',
        context
        )
