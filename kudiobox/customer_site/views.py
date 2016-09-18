from django.shortcuts import render


def home(request):
    context = {
        'page_title': 'Home'
    }
    return render(request, 'customer_site/home.html', context)


def about(request):
    context = {
        'page_title': 'About'
    }
    return render(request, 'customer_site/home.html', context)


def portal(request):
    context = {
        'page_title': 'Home'
    }
    return render(request, 'customer_site/home.html', context)
