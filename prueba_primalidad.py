def es_primo(n1):
    contador = 0


    for i in range(1, n1+1):
        if i == 1 or i == n1:
            continue
        if n1 % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    n1 = int(input('Escribe un numero: '))
    #Se puede obviar el True
    if es_primo(n1): #== True
        print('Es primo carnal')
    else:
        print('Tssssss fallaste')


if __name__ == '__main__':
    run()