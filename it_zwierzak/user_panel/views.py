from django.shortcuts import render, redirect
from .forms import NewUserForm, UserForm, ProfileForm

def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="main/user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })