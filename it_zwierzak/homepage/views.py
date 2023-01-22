from django.shortcuts import render


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
