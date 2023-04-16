print("*******************************************    Inicio del programa    *******************************************\n")
vali= True
while vali==True:
    num= int(input("ingrese la cantidad de datos a procesar "))
    if num > 0:
        vali=False
        posi=0
        nega=0
        nul=0

        for i in range(num):
            valor = input("Ingrese un valor: ")
            if valor.isdigit():
                data=int(valor)
                if data > 0:
                    posi+=1
                elif data < 0:
                    nega+=1
                else:
                    nul+=1
            elif valor.isalpha():
                print("a ingresado una palabra ")
                for i in valor:
                    print(i)
            else:
                print("Probablemente esto es un signo")
        print(f"\nLa cantidad de numeros positivos es {posi}")
        print(f"\nLa cantidad de numeros negativos es {nega}")
        print(f"\nLa cantidad de numeros nulos es {nul}")

    else:
        print("\nEl numero ingresado no es correcto intentalo nuevamente")


print(print("*******************************************    Fin del programa    *******************************************\n"))


