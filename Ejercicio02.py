'''Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50 personas y 1000 personas)
y llame a dos funciones que pongan su nombre en formato capitalizado y calculen la letra de DNI correspondiente.
Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos.'''
import cProfile
import os

def NombreCap(f):
    """Capitaliza los nombres en la lista proporcionada."""
    nombres_capitalizados = []
    for i in f:
        nombre = i.split(',')[0].strip()
        nombres_capitalizados.append(nombre.title())
    return nombres_capitalizados

def CalcularDNI(f):
    """Calcula la letra del DNI para cada línea de la lista."""
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    dnis_calculados = []
    for i in f:
        partes = i.split(',')
        dni_num = int(partes[1].strip())
        letra = letras_dni[dni_num % 23]
        dnis_calculados.append(f"{dni_num}-{letra}")
    return dnis_calculados

def DNI(fichero):
    """Lee el fichero, procesa los nombres y DNIs, y los imprime."""
    if os.path.isfile(fichero):
        with open(fichero, 'r',) as file:
            lista = file.readlines() 
        nombres = NombreCap(lista)
        dnis = CalcularDNI(lista)
        for nombre, dni in zip(nombres, dnis):      #Junta dos listas en una
            print(f"{nombre}: {dni}")
    else:
        print(f"El archivo {fichero} no existe.")
DNI('50.csv')
cProfile.run("DNI('1000.csv')")