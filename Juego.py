# juego_por_rondas.py
from utils import generar_numero_aleatorio

def jugar_una_ronda():
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos = 0
    print("\nEstoy pensando en un número entre 1 y 10. ¡Adivina cuál es!")

    while True:
        intento = input("Tu número: ")

        if not intento.isdigit():
            print("Eso no es un número. Intenta de nuevo.")
            continue

        numero = int(intento)
        intentos += 1

        if numero < numero_secreto:
            print("Muy bajo.\n")
        elif numero > numero_secreto:
            print("Muy alto.\n")
        else:
            print(f"🎉 ¡Correcto! Adivinaste en {intentos} intento(s).")
            break

def iniciar_juego():
    print("🎯 ¡Bienvenido al juego de adivinanza!")
    while True:
        jugar_una_ronda()
        continuar = input("\n¿Quieres jugar otra ronda? (s/n): ").lower()
        if continuar != 's':
            break
    mensaje_despedida()

def mensaje_despedida():
    print("\nGracias por jugar varias rondas. ¡Hasta la próxima!")