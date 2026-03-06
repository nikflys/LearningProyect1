import json
import sys

print("""1. Agregar datos del juego
2. Ver todos los juegos
3. Buscar en la lista de juegos
4. Borrar juego de la lista
5. Salir del programa """)

archivo = None
datos = None

try:
    with open("datos_juegos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("Archivo no encontrado")
except Exception as e:
        print(f"Error inesperado: {e}")

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
        


if eleccion_usuario == 1:
    pass
elif eleccion_usuario == 2:
    print("Aca esta la lista con todos los juegos:")
    print(datos)
elif eleccion_usuario == 3:
    juego_a_buscar = input("Escribi el nombre del juego que queres buscar: ")
    print(juego_a_buscar)
elif eleccion_usuario == 4:
    pass
elif eleccion_usuario == 5:
    sys.exit()
