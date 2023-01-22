from django import render, redirect
from django import redirect
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm

...

def profile(request, username):
    if request.method == 'POST':
        pass

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'user_panel/profile.html', context={'form': form})

    return redirect("homepage")
