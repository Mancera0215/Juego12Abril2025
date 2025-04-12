# juego_con_rango_personalizado.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("🎯 ¡Bienvenido al juego de adivinar números!")

    while True:
        rango_min = input("Ingresa el número mínimo del rango: ")
        rango_max = input("Ingresa el número máximo del rango: ")

        if not (rango_min.isdigit() and rango_max.isdigit()):
            print("Por favor, ingresa solo números.")
            continue

        rango_min = int(rango_min)
        rango_max = int(rango_max)

        if rango_min >= rango_max:
            print("El número mínimo debe ser menor que el máximo. Intenta de nuevo.\n")
            continue

        break

    numero_secreto = generar_numero_aleatorio(rango_min, rango_max)
    intentos = 0

    print(f"\nEstoy pensando en un número entre {rango_min} y {rango_max}. ¡Adivínalo!")

    while True:
        intento = input("Tu número: ")

        if not intento.isdigit():
            print("Eso no es un número válido.")
            continue

        numero = int(intento)
        intentos += 1

        if numero < numero_secreto:
            print("Muy bajo.\n")
        elif numero > numero_secreto:
            print("Muy alto.\n")
        else:
            print(f"🎉 ¡Correcto! Lo lograste en {intentos} intento(s).")
            break

    mensaje_despedida()

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Hasta la próxima!")