from decimal import Decimal
from store.models import Parafernalia

from .models import CatParaf
from itertools import product
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from store.Carrito import Carrito


from .models import Parafernalia


from .models import Parafernalia, Proveedor, CatProve


def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def ofertas_view(request):

    return render(request, 'store/ofertas.html')


def semillas(request):
    context = {}
    return render(request, 'store/semillas.html', context)


from store.models import CatParaf, Parafernalia

def parafernalia_view(request):
    categorias = CatParaf.objects.all()
    categoria_seleccionada = request.GET.getlist('categoria')
    parafernalia_list = filtrar_parafernalia(categoria_seleccionada)

    context = {
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
        'parafernalia_list': parafernalia_list
    }
    return render(request, 'store/parafernalia.html', context)

def filtrar_parafernalia(categorias_seleccionadas):
    if categorias_seleccionadas:
        return Parafernalia.objects.filter(id_cat_paraf__nombre_tipo__in=categorias_seleccionadas)
    else:
        return Parafernalia.objects.all()

def cultivo_view(request):

    return render(request, 'store/cultivo.html')


def contacto_view(request):

    return render(request, 'store/formulario.html')


def login(request):

    return render(request, 'store/entrar.html')


def staff(request):

    return render(request, 'store/staff.html',)


@login_required
def panel_view(request):
    lista_proveedor = Proveedor.objects.all()
    context = {"proveedores": lista_proveedor}
    return render(request, 'store/panel.html', context)


@login_required
def agregar_proveedor(request):
    if request.method == "POST":
        id_prov = request.POST.get("id_prov")
        nombre = request.POST.get("nombre")
        fecha_compra = request.POST.get("fecha_compra")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        direccion = request.POST.get("direccion")
        # Obtener la categoría seleccionada
        id_cat_prove = request.POST.get("id_cat_prove")

        if not fecha_compra:
            messages.error(request, 'La fecha de compra es requerida.')
            return redirect('agregar_proveedor')

        proveedor = Proveedor.objects.create(
            id_prov=id_prov,
            nombre=nombre,
            id_cat_prove_id=id_cat_prove,  # Asignar la categoría al proveedor
            fecha_compra=fecha_compra,
            telefono=telefono,
            email=email,
            direccion=direccion
        )

        messages.success(request, 'Proveedor agregado exitosamente.')
        return redirect('agregar_proveedor')
    else:
        # Obtener todas las categorías de proveedores
        categorias = CatProve.objects.all()
        context = {'categorias': categorias}
        return render(request, 'store/agregar_proveedor.html', context)


def eliminar_proveedor(request, pk):
    try:
        proveedor = Proveedor.objects.get(id_prov=pk)
        proveedor.delete()
        mensaje = "El proveedor se eliminó exitosamente."
    except Proveedor.DoesNotExist:
        mensaje = "El proveedor NO se eliminó."

    lista_proveedores = Proveedor.objects.all()
    context = {"proveedores": lista_proveedores, "mensaje": mensaje}
    return render(request, 'store/panel.html', context)


def buscar_proveedor(request, pk):
    if pk != "":
        try:
            proveedor = Proveedor.objects.get(id_prov=pk)
            context = {"proveedor": proveedor}
            return render(request, 'store/editar_proveedor.html', context)
        except Proveedor.DoesNotExist:
            mensaje = "El proveedor NO existe"
    else:
        mensaje = "El proveedor NO existe"

    lista_proveedores = Proveedor.objects.all()
    context = {"proveedores": lista_proveedores, "mensaje": mensaje}
    return render(request, 'store/panel.html', context)


def modificar_proveedor(request):
    if request.method == "POST":
        id_prov = request.POST["id_prov"]
        nombre = request.POST["nombre"]
        fecha_compra = request.POST["fecha_compra"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        try:
            proveedor = Proveedor.objects.get(id_prov=id_prov)
            proveedor.nombre = nombre
            proveedor.fecha_compra = fecha_compra
            proveedor.telefono = telefono
            proveedor.email = email
            proveedor.direccion = direccion
            proveedor.save()

            mensaje = "Se actualizó el proveedor"
            lista_proveedores = Proveedor.objects.all()
            context = {"proveedores": lista_proveedores, "mensaje": mensaje}
            return render(request, 'store/panel.html', context)
        except Proveedor.DoesNotExist:
            mensaje = "El proveedor NO existe"
            lista_proveedores = Proveedor.objects.all()
            context = {"proveedores": lista_proveedores, "mensaje": mensaje}
            return render(request, 'store/panel.html', context)
    else:
        lista_proveedores = Proveedor.objects.all()
        context = {"proveedores": lista_proveedores}
        return render(request, 'store/panel.html', context)


def carrito(request):
    carrito = Carrito(request)
    # Obtener el total del carrito de la sesión
    total_carrito = carrito.session.get('total_carrito')

    # Realizar el cálculo del precio unitario
    for item in carrito.carrito.values():
        item['precio_unitario'] = item['acumulado'] / item['cantidad']

    context = {
        'carrito': carrito,
        'total_carrito': total_carrito,
    }

    return render(request, 'store/carrito.html', context)


def parafernalia_view(request):
    parafernalia_list = Parafernalia.objects.all()
    context = {'parafernalia_list': parafernalia_list}
    return render(request, 'store/parafernalia.html', context)


def agregar_producto(request, idparaf):
    carrito = Carrito(request)
    parafernalia_obj = Parafernalia.objects.get(idparaf=idparaf)

    # Obtener el precio como float
    precio = float(parafernalia_obj.precio)

    # Agregar la parafernalia al carrito
    carrito.agregar(parafernalia_obj, precio)

    return redirect("parafernalia")


def eliminar_producto(request, idparaf):
    carrito = Carrito(request)
    Parafernalia = Parafernalia.objects.get(idparaf=idparaf)
    carrito.eliminar(Parafernalia)
    return redirect("store/carrito.html")


def restar_producto(request, idparaf):
    carrito = Carrito(request)
    producto = Parafernalia.objects.get(idparaf=idparaf)
    carrito.restar(producto)
    return redirect("carrito")


def sumar_producto(request, idparaf):
    carrito = Carrito(request)
    producto = Parafernalia.objects.get(idparaf=idparaf)
    # Pasar el precio como argumento separado
    carrito.sumar(producto, producto.precio)
    return redirect("carrito")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")
