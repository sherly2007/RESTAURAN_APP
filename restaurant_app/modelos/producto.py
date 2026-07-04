class Producto:
    """Clase padre: representa cualquier producto del restaurante"""
    def __init__(self, nombre: str, precio: float, disponibilidad: bool = True):
        self.nombre = nombre
        self.__precio = precio  # Atributo encapsulado (protegido)
        self.disponibilidad = disponibilidad

    # Método para leer el precio
    def obtener_precio(self) -> float:
        return self.__precio

    # Método para cambiar el precio con regla
    def cambiar_precio(self, nuevo_valor: float) -> None:
        if nuevo_valor > 0:
            self.__precio = nuevo_valor
            print(f"✅ Precio actualizado: {self.nombre} → ${nuevo_valor:.2f}")
        else:
            print("❌ Error: El precio debe ser mayor a cero")

    # Método base para mostrar información
    def mostrar_informacion(self) -> None:
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"Producto: {self.nombre} | Precio: ${self.__precio:.2f} | Estado: {estado}")