from django.shortcuts import render

from .models import Parafernalia

# Create your views here.

# semillas


def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def ofertas_view(request):
    # Lógica de la vista para la página de Ofertas
    return render(request, 'store/ofertas.html')

def semillas(request):
    context = {}
    return render(request, 'store/semillas.html', context)

def parafernalia_view(request):
    parafernalia_list = Parafernalia.objects.all()
    context = {'parafernalia_list': parafernalia_list}
    return render(request, 'store/parafernalia.html', context)

def cultivo_view(request):
    # Lógica de la vista para la página de Cultivo
    return render(request, 'store/cultivo.html')

def contacto_view(request):
    # Lógica de la vista para la página de Contacto
    return render(request, 'store/formulario.html')
    
def login(request):
    # Lógica de la vista para la página de Contacto
    return render(request, 'store/login.html')

def carrito(request):
    # Lógica de la vista para la página de Contacto
    return render(request, 'store/carrito.html')
