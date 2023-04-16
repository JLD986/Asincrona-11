# Obtener la cantidad de números que se van a ingresar
while True:
    try:
        n = int(input("""===========================================
Ingrese la cantidad de números a clasificar
============================================\n"""))
        if n <= 0:
            print("""===========================================
Ingrese un número mayor a cero
===========================================""")
            continue
        break
    except ValueError:
        print("""===========================================
Ingrese un número válido
===========================================\n""")

# Inicializar variables para contar los números
positivos = 0
negativos = 0
nulos = 0

# Obtener los números y clasificarlos por su tipo
for i in range(n):
    while True:
        try:
            num = int(input(f"Ingrese el número {i+1}: "))
            break
        except ValueError:
            print("Ingrese un número válido")
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        nulos += 1

# Mostrar los resultados obtenidos que ingreso el usuario
print(f"La cantidad de números positivos es: {positivos}")
print(f"La cantidad de números negativos es: {negativos}")
print(f"La cantidad de números nulos es: {nulos}")

# Mensaje donde indica la finalizaciond el programa
print("Programa finalizado")


