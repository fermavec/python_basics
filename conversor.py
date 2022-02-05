######## FUNCIONES #######
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuál es la cantidad de Pesos " + tipo_pesos + " a calcular: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print(pesos + " pesos " + tipo_pesos + " son $" + dolares + " dolares")

######## BLOQUES #######
menu = """
Bienvenido al conversor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 97)
elif opcion == 3:
    conversor("Mexicanos", 20)
else:
    print("Elige una opción valida")

