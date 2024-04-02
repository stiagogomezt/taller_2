def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def primos_entre_numeros(numero_inicio, numero_fin):
    total_numeros = numero_fin - numero_inicio + 1
    total_primos = 0

    print("Los números primos entre", numero_inicio, "y", numero_fin, "son:")
    for numero in range(numero_inicio, numero_fin + 1):
        if es_primo(numero):
            total_primos += 1
            print(numero)

    porcentaje_primos = (total_primos / total_numeros) * 100
    print(f"Porcentaje de números primos: {porcentaje_primos:.2f}%")

# Ejemplo de uso de la función
numero_inicio = int(input("Ingresa el número de inicio del rango: "))
numero_fin = int(input("Ingresa el número final del rango: "))
primos_entre_numeros(numero_inicio, numero_fin)