# Agregamos la ruta de la carpeta para que Python encuentre todo
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importaciones exactas
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurant import Restaurante

def main():
    mi_restaurante = Restaurante("El Sabor Casero")

    platillo1 = Platillo ("Arroz con Pollo", 7.50, 20, 600)
    platillo2 = Platillo("Ensalada Mixta", 4.25, 10, 250, disponibilidad=False)

    bebida1 = Bebida("Jugo de Maracuyá", 3.00, 400)
    bebida2 = Bebida("Cerveza Artesanal", 4.75, 500, es_alcoholica=True)

    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    print("\n--- Cambios de precio ---")
    platillo1.cambiar_precio(8.00)
    bebida1.cambiar_precio(-1.00)

    mi_restaurante.mostrar_menu_completo()

if __name__ == "__main__":
    main()