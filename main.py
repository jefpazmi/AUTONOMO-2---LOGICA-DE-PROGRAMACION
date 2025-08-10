# random: sirve para que la computadora pueda elegir aleatoriamente
import random

while True:

    # randrange: genera un entero aleatorio dentro de un rango especificado
    aleatorio = random.randrange(0, 3)
    pc = ""

    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = int(input('Elige tu opcion:'))

    if opcion == 1:
        usuario = "Piedra"
    elif opcion == 2:
        usuario = "Papel"
    elif opcion == 3:
        usuario = "Tijera"
    print("Elegiste:", usuario)

    if aleatorio == 0:
        pc = "Piedra"
    elif aleatorio == 1:
        pc = "Papel"
    elif aleatorio == 2:
        pc = "Tijera"
    print("PC Eligio:", pc)

    if pc == "Piedra" and usuario == "Papel":
        print("GANASTE, papel envuelve piedra")
    elif pc == "Papel" and usuario == "Tijera":
        print("GANASTE, tijera corta papel")
    elif pc == "Tijera" and usuario == "Piedra":
        print("GANASTE, Piedra machaca tijera")
    elif pc == "Papel" and usuario == "Piedra":
        print("PERDISTE, papel envuelve tijera")
    elif pc == "Tijera" and usuario == "Papel":
        print("PERDISTE, tijera corta papel")
    elif pc == "Piedra" and usuario == "Tijera":
        print("PERDISTE, piedra machaca tijera")
    elif pc == usuario:
        print("EMPATE")

