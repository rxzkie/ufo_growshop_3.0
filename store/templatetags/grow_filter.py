from django import template
from store.models import Parafernalia

register = template.Library()

@register.filter
def filtrar_por_categoria(parafernalias, nombre_tipo):
    return parafernalias.filter(id_cat_paraf__nombre_tipo=nombre_tipo)
