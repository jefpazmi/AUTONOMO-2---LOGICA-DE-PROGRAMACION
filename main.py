# random: sirve para que la computadora pueda elegir aleatoriamente
import random

#inicio de la difinicion de la funcion
def jugar_piedra_papel_tijera():
    opciones = ["Piedra", "Papel", "Tijera"]

    # pedir nombre del jugador
    nombre = input("INGRESA TU NOMBRE: ").capitalize()

    while True:
        print("************************************************")
        print(f"*** {nombre.upper()}, DEBES ELEGIR UNA OPCION ***")
        print("************************************************")
        print("Piedra")
        print("Papel")
        print("Tijera")
        print("Salir")

        #capitalize convierte la primera letra a mayúscula para que no importe si el usuario escribe "piedra" o "Piedra"
        usuario = input('ELIGE UNA OPCION : ').capitalize()

        if usuario == "Salir":
            print("**********************************************")
            print(f" Gracias por jugar, {nombre}. ¡Hasta luego!")
            print("**********************************************")
            quit()

        if usuario not in opciones:
            print("**************************************************")
            print(f" Opción no válida. Inténtalo de nuevo. {nombre}")
            continue

        # Elección de la computadora
        pc = random.choice(opciones)

        print("*********************************")
        print(f"\nTú elegiste: {usuario}")
        print(f"La computadora eligió: {pc}\n")
        print("*********************************")

        # Lógica para determinar el ganador
        if usuario == pc:
            print("¡Es un EMPATE!")
            print("**********************************")
        elif (usuario == "Piedra" and pc == "Tijera") or \
                (usuario == "Tijera" and pc == "Papel") or \
                (usuario == "Papel" and pc == "Piedra"):
            print("***********¡GANASTE!*************")
            print("*********************************")
        else:
            print("*****¡LA COMPUTADORA GANA!******")
            print("*********************************")

        # Preguntar si desea seguir jugando
        seguir = input("¿Quieres seguir jugando? (si/no): ").lower()
        if seguir != "si":
            print(f" Gracias por jugar, {nombre}. ¡Hasta luego!")
            break

# Ejecuta el juego
jugar_piedra_papel_tijera()

