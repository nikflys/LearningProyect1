import json
import sys


def accion_biblioteca_juegos(eleccion):
    archivo = None
    datos = None
    
    try:
        with open("datos_juegos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
            print(f"Error inesperado: {e}")
    
    if eleccion == 1:
        nombre_append = input("Cual es el nombre del juego? ")
        release_append = input("Cuando salio el juego? Responde en formato YYYY-MM-DD ")
        while True:
            try:
                precio_append = int(input("Cual es el preico del juego? Solo el numero entero, sin el $: "))
                if type(precio_append) == int:
                    break
            except ValueError:
                print("Dato invalido, tenes que ingresar un numero dentro de las opciones disponibles")
            except Exception as e:
                print(f"Error inesperado: {e}")
        nuevo_juego = {
            "nombre" : nombre_append,
            "release-date" : release_append,
            "price" : precio_append
        }
        if datos is not None:
            datos.append(nuevo_juego)
            if archivo is not None:
                archivo.close()
                with open("datos_juegos.json", "w", encoding="utf-8") as archivo:
                    archivo = json.dump(datos, archivo, indent=4)
    elif eleccion == 2:
        print("Aca esta la lista con todos los juegos:")
        print(datos)
    elif eleccion == 3:
        juego_a_buscar = input("Escribi el nombre del juego que queres buscar: ").lower()
        if datos is not None:
            encontrado = False
            for juego in datos:
                if juego_a_buscar == juego['nombre'].lower():
                    print(f"Encontrado! aca van los datos del juego {juego}")
                    encontrado = True
                    break
            if encontrado == False:
                print("Fijate de haberlo escrito bien, en caso de ser asi, lamentablemente ese juego no lo tenemos todavia.")
    elif eleccion == 4:
        juego_a_borrar = input("Escribi el nombre del juego que queres borrar: ").lower()
        if datos is not None:
            encontrado = False
            i = 0
            for juego in datos:
                if juego_a_borrar == juego['nombre'].lower():
                    if datos is not None:
                        datos.pop(i)
                        if archivo is not None:
                            archivo.close()
                            with open("datos_juegos.json", "w", encoding="utf-8") as archivo:
                                archivo = json.dump(datos, archivo, indent=4)
                    print(f"{juego['nombre']} fue borrado exitosamente!")
                    encontrado = True
                    break
                i += 1
            if encontrado == False:
                print("Fijate de haberlo escrito bien, en caso de ser asi, ese juego no lo tenemos todavia y por ende no lo podemos borrar.")
    elif eleccion == 5:
        print("Hasta luego!")
        sys.exit()