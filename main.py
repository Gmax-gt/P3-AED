import random
from paseo import *

def positivo(mensaje):
    while True:
        numero = int(input(f"{mensaje}: "))

        if not (numero > 0):
            print(f"Fuera de rango [0, inf)")
        else:
            return numero


def entre(menor, mayor, mensaje) :
    while True:
        numero = int(input(f"{mensaje}: "))

        if not (menor <= numero <= mayor):
            print(f"Fuera de rango [{menor}, {mayor}]")
        else:
            break

    return numero

def racaudacion(paseos):
    recaudaciones = [0] * 20
    for i in paseos:

def ordenar (paseos):
    n = len(paseos)

    for i in range (n - 1):
        for j in range (i + 1 ,n):
            if paseos[i].identificacion > paseos[j].identificacion:
                paseos[i],paseos[j] = paseos [j], paseos [i]


def mostrar(paseos):
    for paseo in paseos:
        print (paseo)


def cargar(paseos):
    paseos.clear()
    cantidad = positivo("Cantidad de paseos ")
    nombres = ["Genaro","Joaco","Tuthe","Cr7"]

    for i in range(cantidad):
        identificacion = random.randint (0,9999)
        nombre = random.choice(nombres)
        tipo = random.randint(0,19)
        monto = random. uniform (100, 100)

        paseo = Paseo(identificacion,nombre,tipo,monto)
        paseos.append(paseo)

def menu():
    print("""
    Bienvenido al Menú
    1- Cargar
    2- Mostrar
    3- Recaudacíon por tipo
    4- Buscar 
    5- Salir
        """)

    return int(input("Ingrese una opcion: "))


def principal ():
    paseos = []

    while True:
        opcion=menu()

        if opcion == 1:
            cargar(paseos)
        elif not paseos:
            print("No se cargaron paseos")

        elif opcion == 2:
            ordenar(paseos)
            mostrar(paseos)
        elif opcion == 3:
            racaudacion(paseos)
        elif opcion == 4:
            pass
        elif opcion == 5:
            break
    print ("Fin")

if __name__ == "__main__":
    principal()