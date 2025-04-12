# juego_competencia.py
from utils import generar_numero_aleatorio
import random

def iniciar_juego():
    print("🏁 ¡Bienvenido al juego de adivinanza contra la computadora!")
    rango_min = 1
    rango_max = 10
    numero_secreto = generar_numero_aleatorio(rango_min, rango_max)

    intentos_jugador = 0
    intentos_computadora = 0
    opciones_pc = list(range(rango_min, rango_max + 1))

    print(f"\nEstoy pensando en un número entre {rango_min} y {rango_max}.")

    while True:
        # Turno del jugador
        intento = input("Tu turno (elige un número): ")
        if not intento.isdigit():
            print("Por favor, ingresa un número válido.\n")
            continue

        numero_jugador = int(intento)
        intentos_jugador += 1

        if numero_jugador == numero_secreto:
            print(f"🎉 ¡Ganaste! Adivinaste en {intentos_jugador} intento(s).")
            break
        else:
            if numero_jugador < numero_secreto:
                print("Muy bajo.\n")
            else:
                print("Muy alto.\n")

        # Turno de la computadora
        numero_pc = random.choice(opciones_pc)
        opciones_pc.remove(numero_pc)
        intentos_computadora += 1

        print(f"🤖 La computadora intenta con: {numero_pc}")

        if numero_pc == numero_secreto:
            print(f"💻 ¡La computadora adivinó el número en {intentos_computadora} intento(s)!")
            print("😢 Perdiste esta vez.")
            break

def mensaje_despedida():
    print("\nGracias por jugar. ¡Nos vemos en la próxima competencia!")