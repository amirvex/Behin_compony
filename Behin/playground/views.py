from django.shortcuts import render

import playground


def index(request):
    return render(request, 'playground/templates/pages/index.html')


def about(request):
    return render(request, 'playground/templates/pages/about.html')
