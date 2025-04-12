# adivina_numero.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("¡A ver si puedes adivinar el número que estoy pensando entre 1 y 10!")
    numero_secreto = generar_numero_aleatorio(1, 10)
    cantidad_intentos = 0

    adivinado = False
    while not adivinado:
        intento = input("Tu apuesta: ")

        if not intento.isdigit():
            print("Eso no es un número válido. Intenta nuevamente.")
            continue

        numero = int(intento)
        cantidad_intentos += 1

        if numero < numero_secreto:
            print("Muy bajo, prueba otra vez.\n")
        elif numero > numero_secreto:
            print("Muy alto, intenta de nuevo.\n")
        else:
            print(f"¡Correcto! Descubriste el número en {cantidad_intentos} intento(s).")
            adivinado = True

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Nos vemos pronto!")
