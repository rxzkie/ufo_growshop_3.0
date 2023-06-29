from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm



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
    
    
    return render(request, 'store/staff.html',)





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
