import funciones as fc

while True:
    print("1- sumar")
    print("2- multiplicar")
    print("3- restar")
    print("4- dividir")
    print("5-Para salir")
    opciones=int(input("elija la opcion: "))

    a= int(input("ingrese un numero: "))
    b= int(input("ingrese un numero: "))


    if opciones==1:
        fc.sumar(a,b)
    elif opciones==2:
        fc.multiplicar(a,b)
    elif opciones==3:
        fc.restar(a,b)
    elif opciones==4:
        fc.dividir(a,b)
    elif opciones==5:
        break
    else:
        print("Elija una opcion correcta")
