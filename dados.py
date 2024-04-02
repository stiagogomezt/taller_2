import random

def jugar():
    numero_aleatorio = random.randint(2, 12)
    print("Número aleatorio generado:", numero_aleatorio)
    if numero_aleatorio == 7:
        print("¡Ganó!")
    else:
        print("Deje el juego")

if __name__ == "__main__":
    jugar()
