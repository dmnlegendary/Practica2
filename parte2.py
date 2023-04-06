'''Diaz Jimenez Jorge Arif 3BV2  05/04/2023'''
'''Inciso 4) de la Práctica 2 de la materia "Paradigmas de programación"'''

import random
#import random nos permite acceder a la libreria de funciones random
import datetime
#import datetime nos permite acceder a la libreria de funciones datetime (relacionadas con el manejo de la fecha y hora de nuestro sistema)



#Declaramos la función func_compute(n), donde 'n' es un parámetro recibido de la misma
def func_compute(n):
    return lambda x: x*n #Retorna la multiplicación de un valor 'x' con el parámetro 'n'
'''
El 'lambda' que se encuentra dentro la función 'func_compute(n)' permite que al asignarse un valor 'x' éste se multiplique con el del parámetro 'n'
'''
result = func_compute(2) #La variable 'result' guardara el resultado de operar con func_compute(n); tales que 'n=2' y el parametro 'x' realizando la llamada "result(x)"
print("Double the number of 15 =", result(15)) #Imprime la multiplicacion del valor asignado 'x=15' multiplicado con 'n=2'



#En esta parte aprenderemos sobre el manejo de una lista que tenga varios miembros 
subject_marks =[('English',88),('Science',90),('Maths',97), ('Social sciences',82)] #Asignación de datos a la lista
print("Original list of tuples:")
print(subject_marks) #Imprimimos la lista completa sin modificar
subject_marks.sort(key = lambda x: x[1]) #Se realiza un ordenamiento sobre la lista, empleando como llave distintiva al 2° miembro de cada elemnto del arreglo (La calificación de la materia)
'''
Nota: el método "list.sort(key=None, reverse=False)".Sintaxis extraida de: https://programmerclick.com/article/75431999010/#:~:text=para%20resumir%3A%20sort%20%28%29%20es%20un%20m%C3%A9todo%20de,devuelve%20una%20nueva%20lista%20ordenada%20de%20un%20iterador.
Permite ordenar los elementos de un arreglo si se especifican los parámetros. Explicación extraida de: https://programmerclick.com/article/75431999010/#:~:text=para%20resumir%3A%20sort%20%28%29%20es%20un%20m%C3%A9todo%20de,devuelve%20una%20nueva%20lista%20ordenada%20de%20un%20iterador 
En este caso, lambda recibira cada elemento dentro del arreglo (por ejemplo: ('English',88),('Science',90),...), y gracias a la designación x[1]
solamente escogera al 2° componente de cada elemento, es decir el número. Para finalmente dar continuación al ordenamiento bajo ese parámetro.
'''
print("\nResult:")
print(subject_marks) #Finalmente imprimimos los valores de la lista a manera de que imprima primero el elemento cuyo 2° componente sea menor y por ultimo al elemento cuyo 2° elemento sea mayor



#En esta parte comprenderemos como se realiza el filtrado de valores dentro de una lista
nums = [1,2,3,4,5,6,7,8,9,10] #Asignación de datos a la lista
print("Original list of integers:")
print(nums) #Imprimos todos los valores de nuestra lista original
print("\nnumbers from the said list")
even_nums = list(filter(lambda x: x%2 == 0, nums)) #Filtra los numeros pares de la lista y los guarda en "even_nums"
'''
La técnica list(filter(fn, list)) permite seleccionar unicamente ciertos valores que cumplan con una condición, que seran guardados en otra variabl, para su posterior uso
Sintaxis y explicación extraidas de: https://www.pythontutorial.net/python-basics/python-filter-list/
En nuestro caso particular, a partir de lambda podemos ir sacando cada valor dentro del arreglo y meterlo dentro de 'x' permitiendo evaluarlo y de cumplir
la condición, asignarlo a la nueva variable. Empleado de la misma manera para números pares e impares, lo único que cambia es la condición.
'''
print(even_nums) #Imprime los números pares de la lista
print("\nNumbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums)) #Filtra los números impares de la lista y los guarda en "odd_nums"
print(odd_nums) #Imprime los numeros impares de la lista



#En este segmento analizaremos como operar sobre cada elemento de una lista
nums = [1,2,3,4,5,6,7,8,9,10] #Asignación de datos a la lista
print("Original list of integers:")
print(nums) #Impresión de la lista original
print("\nNumber of the said list:")
square_nums = list(map(lambda x: x**2, nums)) #Cada número de la lista será elevado al cuadrado
'''
list(map(fn, list)) es una técnica que permite operar o manipular sobre cada elemento de un arreglo. Extraido de: https://www.freecodecamp.org/news/python-map-explained-with-examples/
En éste caso particular: la función lambda tomará como valor de entrada a cada uno de los elementos de la lista y devolverá de manera iterada el
número que recibió a la potencia 2 y 3 en las variables "square_nums & cube_nums" respectivamente.
'''
print(square_nums) #Imprime los números de la lista elevados al cuadrado
print("\nEvery number of the said list:")
cube_nums = list(map(lambda x: x**3, nums)) #Eleva cada numero de la lista al cubo
print(cube_nums) #Imprime los números elevados al cubo



#En esta parte analizaremos si una cadena empieza con cierta letra
starts_with = lambda x: True if x.startswith('P') else False #La variable 'starts_with' guarda a la función lambda que determinará si un valor de entrada empieza con la letra 'P'
'''
En nuestra función 'lambda' analizaremos el valor que se le haya asignado como entrada y empleando el evento startswith('N'), compararemos si
el valor de entrada empieza con 'N', de ser afirmativo se devolverá e imprimirá verdadero. Pero si no cumple dicha condición devolverá e imprimirá
falso. (Sólo podra retornar verdadero/falso)
'''
print(starts_with('Python')) #Impresión (Verdadero) si la palabra empieza o no con 'P'
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java')) #Impresión (Falso) si la palabra empieza o no con 'P'



#En esta parte comprenderemos el manejo de datos del sistema referentes a la fecha y hora actuales de nuestro computador
now = datetime.datetime.now() #Guarda en la variable "now" todos los datos del sistem con respecto a la fecha y hora actuales
print(now) #Imprime la hora,día, mes y año actuales
year = lambda x: x.year #la variable "year" guarda el año actual
month = lambda x: x.month #la variable "month" guarda el mes actual
day = lambda x: x.day #la variable "day" guarda el día actual
t = lambda x: x.time() #la variable "t" guarda la hora actual
'''
En el caso de las variables "year, month, day & t" la función lambda permite que al ingresar un dato cómo parámetro dentro de estas variables (Un ejemplo seria t(dato),
en este caso será la fecha y hora, nos permitira extraer únicamente una parte de lo que se le asigne y no todo el bloque de información (Por ejemplo en 't' sólo necesitamos conocer la hora, más no el dia, ni año, etc.).
Lo anterior es útil pues nos permite ahorrar espacio y tiempo ocupados para obtener información específica.
'''
print(year(now)) #Imprime el año actual
print(month(now)) #Imprime el mes actual
print(day(now)) #Imprime el día actual
print(t(now)) #Imprime la hora actual

