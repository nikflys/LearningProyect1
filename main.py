from acciones import accion_biblioteca_juegos

        

if __name__ == "__main__":
    
    print("""1. Agregar un juego
2. Ver todos los juegos
3. Buscar en la lista de juegos
4. Borrar juego de la lista
5. Salir del programa """)

    while True:
        try:
            eleccion_usuario = int(input("Selecciona una de las opciones (1, 2, 3, 4 o 5): "))
            if eleccion_usuario < 1 or eleccion_usuario > 5:
                print("Debes elegir un numero entre el 1 y el 5")
                continue
            break
        except ValueError:
            print("Dato invalido, tenes que ingresar un numero dentro de las opciones disponibles")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    accion_biblioteca_juegos(eleccion_usuario)

