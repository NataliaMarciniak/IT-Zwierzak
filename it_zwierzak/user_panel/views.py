from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditUserForm, EditUserProfileForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    userprofile = user.userprofile
    return render(request, 'accounts/user_detail.html', {'userprofile': userprofile})

def edit_user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = user.userprofile

    user_form = EditUserForm(request.POST or None, instance=user)
    profile_form = EditUserProfileForm(request.POST or None, instance=user_profile)

    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect(f"/accounts/{pk}")

    return render(request, "accounts/user_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })