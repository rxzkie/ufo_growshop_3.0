from django.urls import path
from . import views

from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas/', views.ofertas_view, name='ofertas'),
    path('semillas/', views.semillas, name='semillas'),
    path('parafernalia/', views.parafernalia_view, name='parafernalia'),
    path('cultivo/', views.cultivo_view, name='cultivo'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('entrar/', views.login, name='entrar'),

    path('carrito/', views.carrito, name='carrito'),
    path('staff/', views.staff, name='staff'),
    path('panel/', views.panel_view, name='panel'),
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),  
    
    path('eliminar_proveedor/<str:pk>', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('buscar_proveedor/<str:pk>', views.buscar_proveedor, name='buscar_proveedor'),
    path('modificar-proveedor/', views.modificar_proveedor, name='modificar_proveedor'),

    path('agregar/<int:idparaf>/', views.agregar_producto, name="agregar_producto"),

    path('eliminar/<int:idparaf>/', views.eliminar_producto, name="Del"),

    path('restar/<int:idparaf>/', views.restar_producto, name="Sub"),
    path('sumar/<int:idparaf>/', views.sumar_producto, name="sum"),

    
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('parafernalia/filtrar/', views.filtrar_parafernalia, name='filtrar_parafernalia'),







]