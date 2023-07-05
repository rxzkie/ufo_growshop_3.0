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

    def agregar(self, Parafernalia):
        id = str(Parafernalia.idparaf)  # Asegúrate de usar el atributo correcto para el ID del producto
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": Parafernalia.idparaf,  # Asegúrate de usar el atributo correcto para el ID del producto
                "nombre": Parafernalia.nombre,
                "acumulado": Parafernalia.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += Parafernalia.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, Parafernalia):
        id = str(Parafernalia.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, Parafernalia):
        id = str(Parafernalia.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= Parafernalia.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(Parafernalia)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
