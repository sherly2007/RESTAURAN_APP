from modelos.producto import Producto

class Platillo(Producto):
    """Clase hija: hereda de Producto, representa un plato de comida"""
    def __init__(self, nombre: str, precio: float, tiempo_preparacion: int, calorias: int, disponibilidad: bool = True):
        # Usamos los datos de la clase padre
        super().__init__(nombre, precio, disponibilidad)
        # Atributos propios de los platillos
        self.tiempo_preparacion = tiempo_preparacion
        self.calorias = calorias

    # Sobrescribimos el método para mostrar información distinta
    def mostrar_informacion(self) -> None:
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"🍽️ Platillo: {self.nombre}")
        print(f"   Precio: ${self.obtener_precio():.2f} | Estado: {estado}")
        print(f"   Tiempo de preparación: {self.tiempo_preparacion} min | Calorías: {self.calorias} kcal\n")