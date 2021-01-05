# - *- coding: utf- 8 - *-
import random

def mostrar_tablero(tablero):
    print("\n\tGATO\n")
    print("1     |2     |3")
    print("  " + tablero[0] + "   |   " + tablero[1] + "  |  " + tablero[2] + "   ")
    print("      |      | ")
    print("------+------+------")
    print("4     |5     |6")
    print("  " + tablero[3] + "   |   " + tablero[4] + "  |  " + tablero[5] + "")
    print("      |      | ")
    print("------+------+------")
    print("7     |8     |9")
    print("  " + tablero[6] + "   |   " + tablero[7] + "  |  " + tablero[8] + "")
    print("      |      | ")
    print("\n")

def seguir_jugando():
    print("\n")
    respuesta = input("¿Quieres seguir jugando?").lower()

    if respuesta == "si" or respuesta == "yes":
        return True
    else:
        return False


def ganador(tablero, jugador1, jugador2):
    if jugador1 == "X":
        turno = "Jugador 1"
    else:
        turno = "Jugador 2"
    if tablero[0] == tablero[1] == tablero[2] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[3] == tablero[4] == tablero[5] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[6] == tablero[7] == tablero[8] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[0] == tablero[3] == tablero[6] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[1] == tablero[4] == tablero[7] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[3] == tablero[5] == tablero[8] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[0] == tablero[4] == tablero[8] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True
    elif tablero[2] == tablero[4] == tablero[6] != " ":
        print("\n")
        print("Se acabo la partida")
        print("\n")
        print("El jugador " + turno + " ganó !!")
        return True


def tablero_lleno(tablero):
    for i in tablero:
        if i == " ":
            return False


def casilla_libre(tablero, casilla):
    return tablero[casilla] == " "


def mov_jugador1(tablero):
    posicion = None;
    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        if posicion not in posiciones:
            posicion = input("Escoge la casilla (1-9): ")

            return posicion - 1
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("Esta posición ha sido ocupada, porfavor ingresa otro número")
            else:
                return posicion - 1

def mov_jugador2(tablero, jugador2, jugador1):
    posicion = None;
    posiciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        if posicion not in posiciones:
            posicion = int(input("Escoge la casilla (1-9): "))
            return posicion - 1
        else:
            posicion = int(posicion)
            if not casilla_libre(tablero, posicion-1):
                print("Esta posición ha sido ocupada, porfavor ingresa otro número")
            else:
                return posicion - 1

def juego():
    turno = "Jugador 1"
    jugador1 = "X";
    jugador2 = "O";
    jugando = True

    while jugando:
        tablero = [" "] * 9

        mostrar_tablero(tablero)

        partida = True
        while partida:
            if tablero_lleno(tablero):
                print("Empate")
                partida = False

            elif turno == "Jugador 1":
                casilla = mov_jugador1(tablero)
                tablero[casilla] = jugador1
                turno = "Jugador 2"
                mostrar_tablero(tablero)
                ganador(tablero, jugador1, jugador2)

            elif turno == "Jugador 2":
                casilla = mov_jugador2(tablero, jugador2, jugador1)
                tablero[casilla] = jugador2
                turno = "Jugador 1"
                mostrar_tablero(tablero)
                ganador(tablero, jugador2, jugador1)

        jugando = seguir_jugando()


juego()