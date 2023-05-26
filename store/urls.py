from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('semillas/', views.semillas, name='semillas'),
    path('ofertas/', views.ofertas_view, name='ofertas'),
    path('semillas/', views.semillas_view, name='semillas'),
    path('parafernalia/', views.parafernalia_view, name='parafernalia'),
    path('cultivo/', views.cultivo_view, name='cultivo'),
    path('contacto/', views.contacto_view, name='contacto'),
]