'''Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50 personas y 1000 personas)
y llame a dos funciones que pongan su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos.'''

def NombreCap(f):
    a = 0

def CalcularDNI(f):
    a = {0:'T',1:'R',2:'W',3:''}
    for i in f:
        p = i.split(',')
        p[1].strip()


def DNI(fichero):
    import os
    if os.path.isfile(fichero):
        with open (fichero, 'r'):
            for linea in fichero:
                lista = fichero.readline()
        NombreCap(lista)
        CalcularDNI(lista)
DNI('50.csv')