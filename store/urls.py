from django.urls import path
from . import views

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('ofertas/', views.ofertas_view, name='ofertas'),
    path('semillas/', views.semillas, name='semillas'),
    path('parafernalia/', views.parafernalia_view, name='parafernalia'),
    path('cultivo/', views.cultivo_view, name='cultivo'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('login/', views.login, name='login'),
    path('carrito/', views.carrito, name='carrito'),
    path('staff/', views.staff, name='staff'),
     path('panel/', views.panel_view, name='panel'),
      path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),  # Nueva URL para agregar proveedor



]