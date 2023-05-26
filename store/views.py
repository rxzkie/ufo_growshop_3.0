from django.shortcuts import render

# Create your views here.

# semillas


def index(request):
    context = {}
    return render(request, 'store/index.html', context)

def semillas(request):
    context = {}
    return render(request, 'store/semillas.html', context)