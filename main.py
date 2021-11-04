import random

def showDashboard(dashboard):
    print("\n\tTIC TAC TOE\n")
    print("1     |2     |3")
    print("  " + dashboard[0] + "   |   " + dashboard[1] + "  |  " + dashboard[2] + "   ")
    print("      |      | ")
    print("------+------+------")
    print("4     |5     |6")
    print("  " + dashboard[3] + "   |   " + dashboard[4] + "  |  " + dashboard[5] + "")
    print("      |      | ")
    print("------+------+------")
    print("7     |8     |9")
    print("  " + dashboard[6] + "   |   " + dashboard[7] + "  |  " + dashboard[8] + "")
    print("      |      | ")
    print("\n")

def keepPlaying():
    print("\n")
    answer = input("¿Quieres seguir jugando?").lower()

    if answer == "si" or answer == "yes":
        return True
    else:
        return False


def win(dashboard, player):
    if player == "X":
        shift = "Jugador 1"
    else:
        shift = "Jugador 2"

    if dashboard[0] == dashboard[1] == dashboard[2] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[3] == dashboard[4] == dashboard[5] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[6] == dashboard[7] == dashboard[8] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[0] == dashboard[3] == dashboard[6] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[1] == dashboard[4] == dashboard[7] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[3] == dashboard[5] == dashboard[8] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[0] == dashboard[4] == dashboard[8] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False
    elif dashboard[2] == dashboard[4] == dashboard[6] != " ":
        print("\n")
        print("Se acabó la partida")
        print("\n")
        print("El " + shift + " ganó")
        return False

    return True


def fullDashboard(dashboard):
    for i in dashboard:
        if i == " ":
            return False


def freeBox(dashboard, box):
    return dashboard[box] == " "


def player1Move(dashboard):
    position = None;
    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if position not in positions:
        position = int(input("Escoge la casilla (1-9): "))

        return (position - 1)
    else:
        position = int(position)
        if not freeBox(dashboard, (position - 1)):
            print("Esta posición ha sido ocupada, porfavor ingresa otro número")
        else:
            return (position - 1)

def player2Move(dashboard):
    position = None;
    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if position not in positions:
        position = int(input("Escoge la casilla (1-9): "))
        return (position - 1)
    else:
        position = int(position)
        if not freeBox(dashboard, (position - 1)):
            print("Esta posición ha sido ocupada, porfavor ingresa otro número")
        else:
            return (position - 1)

def play():
    shift = "Jugador 1"
    player1 = "X";
    player2 = "O";
    playing = True

    while playing:
        dashboard = [" "] * 9

        showDashboard(dashboard)

        game = True
        while game:
            if fullDashboard(dashboard):
                print("Empate")
                game = False

            if shift == "Jugador 1":
                box = player1Move(dashboard)
                dashboard[box] = player1
                shift = "Jugador 2"
                showDashboard(dashboard)
                game = win(dashboard, player1)

            elif shift == "Jugador 2":
                box = player2Move(dashboard)
                dashboard[box] = player2
                shift = "Jugador 1"
                showDashboard(dashboard)
                game = win(dashboard, player2)

        playing = keepPlaying()

play()
