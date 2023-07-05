from decimal import Decimal, InvalidOperation

def total_carrito(request):
    total = Decimal('0.00')

    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                try:
                    total += Decimal(value["acumulado"])
                except InvalidOperation:
                    # Manejar el error de conversión
                    # Puedes imprimir un mensaje de error o tomar alguna otra acción apropiada
                    print(f"Error de conversión en 'acumulado': {value['acumulado']}")

    return {"total_carrito": total}
