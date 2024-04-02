while True:
    try:
        numero_entero = int(input("Por favor, ingresa un número entero mayor que 0: "))
        if numero_entero > 0:
            break
        else:
            print("El número ingresado debe ser mayor que 0. Intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Imprimir el número ingresado por el usuario
print("El número que ingresaste es:", numero_entero)
