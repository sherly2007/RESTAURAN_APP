from modelos.producto import Producto

class Bebida(Producto):
    """Clase hija: hereda de Producto, representa una bebida"""
    def __init__(self, nombre: str, precio: float, volumen_ml: int, es_alcoholica: bool = False, disponibilidad: bool = True):
        # Usamos los datos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        # Atributos propios de las bebidas
        self.volumen_ml = volumen_ml
        self.es_alcoholica = es_alcoholica

    # Sobrescribimos el método para mostrar información distinta
    def mostrar_informacion(self) -> None:
        tipo = "Alcohólica" if self.es_alcoholica else "Sin alcohol"
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"🥤 Bebida: {self.nombre}")
        print(f"   Precio: ${self.obtener_precio():.2f} | Estado: {estado}")
        print(f"   Volumen: {self.volumen_ml} ml | Tipo: {tipo}\n")