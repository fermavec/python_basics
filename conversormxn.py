pesos = input("Cuál es la cantidad de Pesos a calcular: ")
pesos = float(pesos)
valor_dolar = 20
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
pesos = round(pesos, 2)
pesos = str(pesos)
print(pesos + " mxn son $" + dolares + " dolares")