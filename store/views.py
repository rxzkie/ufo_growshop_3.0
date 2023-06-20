from django.shortcuts import render

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
    if request.method != "POST":
        lista_generos = Genero.objects.all()
        context = {"generos":lista_generos}
        return render(request,'venta/alumnos_add.html', context)
    else:
        #izq: variable local - der: input del formulario (name)
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apePaterno = request.POST["apePat"]
        apeMaterno = request.POST["apeMat"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"] #id_genero (value)
        telefono = request.POST["telefono"]
        mail = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)
        #se crea onjeto alumno, izq: campo del model - der: variable local
        objAlumno = Alumno.objects.create(
            rut              = rut,
            nombre           = nombre,
            apellido_paterno = apePaterno,
            apellido_materno = apeMaterno,
            fecha_nacimiento = fechaNac,
            id_genero        = objGenero,
            telefono         = telefono,
            email            = mail,
            direccion        = direccion,
            activo           = 1)
        
        objAlumno.save() #insert 
        lista_generos = Genero.objects.all()
        context = {"mensaje":"Se guardó alumno", "generos":lista_generos}
        return render(request,'venta/alumnos_add.html', context)
