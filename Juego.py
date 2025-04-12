# adivina_numero_personalizado.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("¡Bienvenido al juego de adivinar números!")
    
    while True:
        rango_max = input("Elige el número máximo para adivinar (ejemplo: 10, 50, 100): ")
        if rango_max.isdigit() and int(rango_max) > 1:
            rango_max = int(rango_max)
            break
        else:
            print("Por favor, ingresa un número válido mayor a 1.")
    
    numero_secreto = generar_numero_aleatorio(1, rango_max)
    intentos = 0

    while True:
        intento = input(f"Adivina un número entre 1 y {rango_max}: ")

        if not intento.isdigit():
            print("Eso no es un número. Intenta nuevamente.")
            continue

        numero = int(intento)
        intentos += 1

        if numero < numero_secreto:
            print("Muy bajo.\n")
        elif numero > numero_secreto:
            print("Muy alto.\n")
        else:
            print(f"¡Lo lograste! Adivinaste el número en {intentos} intento(s).")
            break

def mensaje_despedida():
    print("\n¡Gracias por jugar, vuelve pronto!")