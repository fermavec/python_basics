def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


#Variable de inicio siempre
def run():
    print('Un palindromo es una frase o palabra que se lee igual en ambas direcciones')
    palabra=input('Ingrese un palindromo: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


#entry point
if __name__ == '__main__':
    run()