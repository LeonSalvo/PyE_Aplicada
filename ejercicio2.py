import random

def throw_dice():
    return random.randint(1, 6)

def juanceto01():
    dice1 = throw_dice()
    dice2 = throw_dice()
    if dice1 != 4 and dice2 != 4:
        dice1 = throw_dice()
        dice2 = throw_dice()
    elif dice1 == 4 or dice2 == 4:
        if dice1 < 4:
            dice1 = throw_dice()
        elif dice2 < 4:
            dice2 = throw_dice()
    return (dice1, dice2)

##A CAMBIAR
##Hay que hacer la mejor jugada posible teniendo en cuenta el puntaje de juaN
##---------------------------------------------------------------------------------
def maria_antonieta(juanceto01): ##el puntaje de juanceto01
    dice1 = throw_dice()
    dice2 = throw_dice()
    if dice1 != 4 and dice2 != 4:
        dice1 = throw_dice()
        dice2 = throw_dice()
    elif dice1 == 4 or dice2 == 4:
        if dice1 == 4:
            if dice2 < juanceto01:
                dice2 = throw_dice()
        elif dice2 == 4:
            if dice1 < juanceto01:
                dice1 = throw_dice()
    return (dice1, dice2)

##---------------------------------------------------------------------------------

def points_calculator(player):
    points = 0
    if player[0] == 4:
        points = player[1]
    elif player[1] == 4:
        points = player[0]
    return points

def game():
    juan = points_calculator(juanceto01())
    maria = points_calculator(maria_antonieta(juan))
    if juan > maria:
        print(f"Juan gana con {juan} puntos")
        return 0
    elif maria > juan:
        print("Maria gana con {maria} puntos")
        return 1
    else:
        print("Hubo un empate con {juan} puntos")
        return 2
    
def calculate_probability(iterations):
    juan_wins = 0
    maria_wins = 0
    ties = 0
    for i in range(iterations):
        result = game()
        if result == 0:
            juan_wins += 1
        elif result == 1:
            maria_wins += 1
        else:
            ties += 1
    print(f"Probabilidad de que Juan gane: {juan_wins/iterations}")
    print(f"Probabilidad de que Maria gane: {maria_wins/iterations}")
    print(f"Probabilidad de empate: {ties/iterations}")

def main():
    print('Ejercicio 2')
    print('Juego de los dados')
    print('1. Iterar 1000 veces')
    print('2. Iterar 10000 veces')
    print('3. Iterar 100000 veces')
    
    iterations = int(input('Seleccione una opción: '))
    if iterations == 1:
        calculate_probability(1000)
    elif iterations == 2:
        calculate_probability(10000)
    elif iterations == 3:
        calculate_probability(100000)
    else:
        print('Opción no válida')

    
    