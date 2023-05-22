from django.shortcuts import render

# Create your views here.

# semillas

def semillas(request):
    context={}
    return render(request, 'store/semillas.html', context)