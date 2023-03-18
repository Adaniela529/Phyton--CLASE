print("Bienvenido al menú interactivo")
while True:
    print(""" Elige una opción
    1) Dibujar un cuadrado
    2) Hallar si el numero es multiplo de 2 en una serie de numeros
    3) Salir""")
    
    opcion = input() # me devuelve un string ''
    if opcion == '1':
        lado=int(input("Ingrese lado del cuadrado: "))
        for i in range(0,lado):
            for j in range(0,lado):
                print("*",end="")
                print()
    elif opcion == '2':
        n2 = int(input("Ingrese un numero del 1 al 20: "))
        if n2 % 2 == 0:
            print(f"El numero {n2} es multiplo de 2")         
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
