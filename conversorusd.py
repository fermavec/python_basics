dolares = input("Cuál es la cantidad de Dólares a calcular: ")
dolares = float(dolares)
valor_pesos = 20
pesos = dolares * valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
dolares = round(dolares, 2)
dolares = str(dolares)
print(dolares + " usd son " + pesos + " mxn")