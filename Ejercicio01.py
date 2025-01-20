'''
Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci
asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta.
'''
import datetime

def fibonacci(n):
    a, b = 0,1
    for i in range(n):
        a, b = b, a + b
    return a

comienzo = datetime.datetime.now()
print (fibonacci(40))
final = datetime.datetime.now()
print('Ha tardado ', final - comienzo)


def recursiva(n):
    if n <= 1:
        return n
    return recursiva(n-1) + recursiva(n-2)

comienzo = datetime.datetime.now()
print(recursiva(40))
final = datetime.datetime.now()
print('Ha tardado ', final - comienzo)