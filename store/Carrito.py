

from decimal import Decimal


class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto, precio):
            id = int(producto.idparaf)
            if id not in self.carrito.keys():
                self.carrito[id] = {
                    "producto_id": producto.idparaf,
                    "nombre": producto.nombre,
                    "acumulado": int(precio),
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += int(precio)
            self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = int(producto.idparaf)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()



    def restar(self, producto):
        idparaf = str(producto.idparaf)
        if idparaf in self.carrito:
            if self.carrito[idparaf]['cantidad'] > 1:
                self.carrito[idparaf]['cantidad'] -= 1
                self.carrito[idparaf]['acumulado'] -= Decimal(str(producto.precio))
            else:
                del self.carrito[idparaf]
            self.guardar_carrito()

    def sumar(self, producto):
        idparaf = str(producto.idparaf)
        if idparaf in self.carrito:
            self.carrito[idparaf]['cantidad'] += 1
            self.carrito[idparaf]['acumulado'] += Decimal(str(producto.precio))
            self.guardar_carrito()

    def limpiar(self):
            self.carrito = {}
            self.guardar_carrito()
