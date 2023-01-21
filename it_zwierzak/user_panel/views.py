from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def my_profile(request):
    return render(
        request,
        'user_panel/my_profile.html'
    )


def adoptions(request):
    return render(
        request,
        'user_panel/adoptions.html'
    )


def favourite(request):
    return render(
        request,
        'user_panel/favourite.html'
    )


def user_data(request):
    return render(
        request,
        'user_panel/user_data.html'
    )
