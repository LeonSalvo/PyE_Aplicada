import random

def monty_hall(choice):
    # Creamos una lista de 3 elementos, donde cada elemento representa una puerta, el valor True indica que la puerta contiene el auto
    # Elegimos una puerta aleatoria para que contenga el auto y otra puerta aleatoria que representa la elección del participante
    doors = [False] * 3
    rnd = random.randint(0,2)
    doors[rnd] = True
    rnd_choice = random.randint(0,2)
    print(f'Puerta elegida por el participante: {rnd_choice}')
    print(f'Puerta que contiene el auto: {rnd}')
    check = True
    # El presentador abre una puerta que no contiene el auto y que no fue seleccionada por el participante
    while check:
        rnd_presenter = random.randint(0,2)
        if not doors[rnd_presenter] and rnd_presenter != rnd_choice:
            check = False
    print(f'Puerta abierta por el presentador: {rnd_presenter}')
    # Si el participante decide cambiar de puerta, se cambia la puerta seleccionada por una puerta que no fue seleccionada ni abierta por el presentador
    if choice:
        for i in range(3):
            if i != rnd_choice and i != rnd_presenter:
                rnd_choice = i
                print(f'El participante cambio de puerta, la nueva puerta seleccionada es: {rnd_choice}')
                break
    if doors[rnd_choice]:
        print('El participante ganó')
    else:
        print('El participante perdió')
    return doors[rnd_choice]


def calculate_probability(choice, iterations):
    win = 0
    for i in range(iterations):
        if monty_hall(choice):
            win += 1
        # Usamos random.seed() para cambiar la "semilla" y asi obtener números aleatorios diferentes
        random.seed()
        print('---------------------')

    if choice:
        print(f'Probabilidad de ganar si cambia de puerta: {win/iterations}')
    else:
        print(f'Probabilidad de ganar si no cambia de puerta: {win/iterations}')

def main():
    print('Ejercicio 1')
    print('Simulación del juego Monty Hall')
    print('1. Cambiar de puerta')
    print('2. No cambiar de puerta')
    choice = int(input('Seleccione una opción: '))
    print('1. Iterar 1000 veces')
    print('2. Iterar 10000 veces')
    print('3. Iterar 100000 veces')
    iterations = int(input('Seleccione una opción: '))
    if iterations == 1:
        calculate_probability(choice == 1, 1000)
    elif iterations == 2:
        calculate_probability(choice == 1, 10000)
    elif iterations == 3:
        calculate_probability(choice == 1, 100000)
    else:
        print('Opción no válida')


main()