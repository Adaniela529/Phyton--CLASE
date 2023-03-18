def MayorNumero(x,y):
    if x > y:
        return x
    elif y> x:
        return y
    else:
        return 0
    


    a=int(input("Ingrese el primer numero: "))
    b=int(input("Ingrese el segundo numero: "))

    i= MayorNumero(a,b)
    if i==0:
        print("Los numeros son iguales")
    else:
        print(f"El numero mayor es:{i}")
