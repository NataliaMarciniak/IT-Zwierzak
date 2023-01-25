from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Profile
from .forms import UserEditForm, ProfileEditForm


@login_required
def edit(request):
    if request.method == 'POST':
     user_form = UserEditForm(instance=request.user,
                              data=request.POST)
     profile_form = ProfileEditForm(instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
     if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
     else:
      user_form = UserEditForm(instance=request.user)
      profile_form = ProfileEditForm(instance=request.user.profile)
      return render(request,
                    'user_panel/edit.html',
                    {'user_form': user_form,
                     'profile_form': profile_form})