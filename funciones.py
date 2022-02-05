#Funciones
#def imprimir_mensajes():
#    print('Mensaje especial: ')
#    print('Estoy aprendiendo a usar funciones')

# imprimir_mensajes()
# imprimir_mensajes()
# imprimir_mensajes()

# Paramentros para Funciones
def conversacion(mensaje):
    print('Hola')
    print('Cómo estás')
    print(mensaje)
    print('Adios')

opcion= input('Elige una opción (1, 2 o 3): ')
#estoy dejando a proposito el entero eb string para poder concatenar
if opcion=='1':
    conversacion('Elegiste la opción: ' + opcion)
    #print('Hola')
    #print('Cómo estás')
    #print('Elegiste la opción 1')
    #print('Adios')
elif opcion=='2':
    conversacion('Elegiste la opción: ' + opcion)
    #print('Hola')
    #print('Cómo estás')
    #print('Elegiste la opción 2')
    #print('Adios')
elif opcion=='3':
    conversacion('Elegiste la opción: ' + opcion)
    #print('Hola')
    #print('Cómo estás')
    #print('Elegiste la opción 3')
    #print('Adios')
else:
    conversacion('Elegiste una opción invalida ')
    #print('Hola')
    #print('Cómo estás')
    #print('Elegiste incorrectamente')
    #print('Adios')