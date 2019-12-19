# Programa que se comportacomo una calculadora
"""
Curso de raspberry Pi

by Darwin Eventur
Diciembre 2019
Licencia CC
"""
repetir = True  # Variable para decidir si se repite
while repetir == True:
    a = input("Dime el primero numero: ")
    b = input("Dime el segundo numero: ")
    operacion = input("Dime la operacion (+-/*) ")
    if operacion == "+" :
        c = int(a) + int(b)
        print("La suma es " + str(c) )
    elif operacion == "-" :
        c = int(a) - int(b)
        print("La diferencia es " + str(c) )
    elif operacion == "/" :
        c = int(a) / int(b)
        print("La division es " + str(c) )
    elif operacion == "*" :
        c = int(a) * int(b)
        print("El producto es " + str(c) )
    else :
        print("Sólo sé calcular +-/*")
    quiereRepetir = input("¿Quieres hacer más operaciones"?)
    if quiereRepetir != "S" and quiereRepetir !== "Si" :
        repetir = False