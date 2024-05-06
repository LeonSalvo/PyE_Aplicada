import random

# Función que simula el lanzamiento de un dado.
def throw_dice():
    return random.randint(1, 6)

# Función que simula el turno de Juan, dependiendo de los dados que saque.
def juan_turn():
    dice1 = throw_dice()
    dice2 = throw_dice()

    # Re-lanzar si no hay un 4.
    if dice1 != 4 and dice2 != 4:
        dice1 = throw_dice()
        dice2 = throw_dice()

    # Re-lanzar si hay un 4 y el otro dado es menor al puntaje actual de Juan
    elif dice1 == 4 or dice2 == 4:
        if dice1 < 4:
            dice1 = throw_dice()
        elif dice2 < 4:
            dice2 = throw_dice()
    return (dice1, dice2)

# A CAMBIAR
# Hay que hacer la mejor jugada posible teniendo en cuenta el puntaje de Juan.

# Funcion que simula el turno de Maria, dependiendo de los puntos de Juan.
def maria_turn(juans_points): # El puntaje de Juan.
    dice1 = throw_dice()
    dice2 = throw_dice()

    # Re-lanzar si no hay un 4
    if dice1 != 4 and dice2 != 4:
        dice1 = throw_dice()
        dice2 = throw_dice()
    elif dice1 == 4:
        # Re-lanzar si hay un 4 y el otro dado es menor al puntaje de Juan
        if dice2 < juans_points:
            dice2 = throw_dice()
    elif dice2 == 4:
        if dice1 < juans_points:
            dice1 = throw_dice()
    return (dice1, dice2)

# Función para calcular el puntaje de un jugador.
def points_calculator(player):
    points = 0
    if player[0] == 4:
        points = player[1]
    elif player[1] == 4:
        points = player[0]
    return points

# Función que simula el juego entre Juan y Maria, devuelve el ganador.
def game():
    random.seed() # Para que los números aleatorios sean diferentes en cada ejecución.
    # Turno de Juan
    juan = points_calculator(juan_turn())
    
    # Turno de María.
    maria = points_calculator(maria_turn(juan))
    
    # Determinar el ganador.
    if juan > maria:
        print(f"Juan gana con {juan} puntos")
        return 0
    elif maria > juan:
        print(f"Maria gana con {maria} puntos")
        return 1
    else:
        print(f"Hubo un empate con {juan} puntos")
        return 2

# Función que calcula la probabilidad de que Juan o Maria ganen.
def calculate_probability(iterations):
    juan_wins = 0
    maria_wins = 0
    ties = 0 # Empates.
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

# Función principal.
def main():
    print('Ejercicio 2')
    print('Juego de los dados')
    print('1. Iterar 1000 veces')
    print('2. Iterar 10000 veces')
    print('3. Iterar 100000 veces')
    
    try:
        iterations = int(input('Seleccione una opción: '))
    except ValueError:
        print('Entrada inválida. Solo se permiten números.\n')
        return main()
    
    if iterations == 1:
        calculate_probability(1000)
    elif iterations == 2:
        calculate_probability(10000)
    elif iterations == 3:
        calculate_probability(100000)
    else:
        print('Opción no válida.\n')

    
main()