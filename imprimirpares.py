def impares_entre_numeros(numero_inicio, numero_fin):
    # Verificar que el número de inicio sea menor que el número final
    if numero_inicio >= numero_fin:
        print("El número de inicio debe ser menor que el número final.")
        return
    
    print("Los números pares entre", numero_inicio, "y", numero_fin, "son:")
    # Iterar a través del rango desde el número de inicio hasta el número final
    for i in range(numero_inicio, numero_fin + 1):
        # Verificar si el número actual es par
        if i % 2 == 0:
            print(i)