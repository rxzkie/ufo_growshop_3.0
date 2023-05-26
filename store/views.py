from django.shortcuts import render

# Create your views here.

# semillas


def index(request):
    context = {}
    return render(request, 'store/index.html', context)

def semillas(request):
    context = {}
    return render(request, 'store/semillas.html', context)


def ofertas_view(request):
    # Lógica de la vista para la página de Ofertas
    return render(request, 'store/ofertas.html')


def parafernalia_view(request):
    # Lógica de la vista para la página de Parafernalia
    return render(request, 'store/parafernalia.html')

def cultivo_view(request):
    # Lógica de la vista para la página de Cultivo
    return render(request, 'store/cultivo.html')

def contacto_view(request):
    # Lógica de la vista para la página de Contacto
    return render(request, 'store/contacto.html')
