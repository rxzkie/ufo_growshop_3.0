from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Parafernalia, Proveedor


def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def ofertas_view(request):

    return render(request, 'store/ofertas.html')


def semillas(request):
    context = {}
    return render(request, 'store/semillas.html', context)


def parafernalia_view(request):
    parafernalia_list = Parafernalia.objects.all()
    context = {'parafernalia_list': parafernalia_list}
    return render(request, 'store/parafernalia.html', context)


def cultivo_view(request):

    return render(request, 'store/cultivo.html')


def contacto_view(request):

    return render(request, 'store/formulario.html')


def login(request):

    return render(request, 'store/login.html')


def carrito(request):

    return render(request, 'store/carrito.html')


def staff(request):

    return render(request, 'store/staff.html')


def panel_view(request):
    lista_proveedor = Proveedor.objects.all()
    context = {"proveedores": lista_proveedor}
    return render(request, 'store/panel.html', context)


def agregar_proveedor(request):
    if request.method == "POST":
        id_prov = request.POST.get("id_prov")
        nombre = request.POST.get("nombre")
        fecha_compra = request.POST.get("fecha_compra")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        direccion = request.POST.get("direccion")

        proveedor = Proveedor(
            id_prov=id_prov,
            nombre=nombre,
            fecha_compra=fecha_compra,
            telefono=telefono,
            email=email,
            direccion=direccion
        )

        proveedor.save()
        messages.success(request, 'Proveedor agregado exitosamente.')

    return render(request, 'store/agregar_proveedor.html')
