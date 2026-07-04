class Restaurante:
    """Clase de servicio: administra todos los productos del menú"""
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.__lista_productos = []  # Lista protegida

    # Método para agregar productos
    def agregar_producto(self, producto):
        self.__lista_productos.append(producto)
        print(f"📦 Producto agregado: {producto.nombre}")

    # Método para mostrar todo el menú
    def mostrar_menu_completo(self):
        print(f"\n===== MENÚ DE {self.nombre_restaurante.upper()} =====")
        if not self.__lista_productos:
            print("El menú no tiene productos registrados.")
            return
        # Aquí se aplica el polimorfismo
        for item in self.__lista_productos:
            item.mostrar_informacion()