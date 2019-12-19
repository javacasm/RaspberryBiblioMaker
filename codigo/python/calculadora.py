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
    print("Sólo se calcular +-/*")
