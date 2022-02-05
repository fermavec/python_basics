import random


def run():
    aleatorio = random.randint(1, 100)
    n_usuario = int(input('¿Qué numero estoy pendando (1 a 100): '))
    while aleatorio != n_usuario:
        if n_usuario < aleatorio:
            print('Echale más')
        else:
            print('Tssss... te pasaste')
        n_usuario = int(input('¿Qué numero estoy pendando (1 a 100): '))
    print('¿Ves que facil?')


if __name__ == '__main__':
    run()