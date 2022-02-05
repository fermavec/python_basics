def run():
    #for contador in range(1000):
        #if contador % 2 != 0:
        #    continue
        #print(contador)


        #for i in range(10000):
        #    print(i)
        #    if i == 200:
        #        break


        nombre=input('ingresa un nombre: ')
        for letra in nombre:
            if letra == 'o':
                break
            print(letra)


if __name__ == '__main__':
    run()