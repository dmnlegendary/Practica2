'''Díaz Jiménez Jorge Arif 3BV2  05/04/2023'''
'''Incisios 1), 2) y 3) de la práctica 2 de la materia "Paradigmas de Programación"'''

import random
#import random nos permite acceder a la libreria de funciones random

entradaX = int(input("Ingrese un número sobre el cual realizar operaciones: "))
print("")
entradaY = int(input("Ingrese un número secundario sobre el cual realizar operaciones: "))
print("")
#"entradaX" y "entradaY" son variables que almacenarán un valor ingresado por el usuario

print("El valor de entrada es: ", entradaX)
print("El valor de entrada secundario es: ", entradaY)
#Imprimimos los valores de entrada recibidos

#Nota: todas las funciones que aquí se presenten serán operadas con el valor ingresado por el usuario

#Definamos el comportamiento de la función suma()
def suma():
    return lambda x: x+15 #Retorna la suma de un número 'x' con 15 (Nota: x ha sido previamente ingresado por el usuario)
valueX = suma()
print("El resultado de esta primera parte es: ", valueX(entradaX)) #Impresión del valor ingresado por el usuario más 15

#Definicion del comportamiento de la función multiplicacion()
def multiplicacion():
    return lambda x,y: x*y #Retorna la multiplicación de los valores 'x' y 'y' (Nota: Ambos previamente ingresados por el usuario)
valueXY = multiplicacion()
print("\n\nMultiplicar X, Y da: ", valueXY(entradaX, entradaY)) #Impresión de la multiplicación de entradaX con entradaY

#Definición del comportamiento de la función division()
def division():
    aleatorio = random.randint(1,10) #Generá un número aleatorio entre 1 y 10
    print("\n\nEl numero aleatorio generado es: ", aleatorio)
    return lambda x: x/aleatorio #Retorna la división entre el dato de entrada 'x' (previamente ingresado por el usuario) con el número aleatorio guardado en la variable 'aleatorio'
cosa = division() 
print("\nDividir valor de entrada con el valor aleatorio previamente asignado da como resultado: ", cosa(entradaX))#Impresión de dividir el valor de entrada con un número aleatorio
