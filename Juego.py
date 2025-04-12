# juego_contra_reloj.py
import time
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("⏱️ ¡Bienvenido al reto contra el reloj!")
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos = 0

    print(f"\nTienes 30 segundos para adivinar el número entre 1 y 10. ¡Que empiece el desafío!")

    # Empezamos el cronómetro
    tiempo_inicio = time.time()

    while True:
        intento = input("Tu número: ")

        if not intento.isdigit():
            print("Eso no es un número. Intenta de nuevo.\n")
            continue

        numero = int(intento)
        intentos += 1

        # Verificar el tiempo
        tiempo_restante = 30 - (time.time() - tiempo_inicio)

        if tiempo_restante <= 0:
            print(f"\n⏳ ¡Se acabó el tiempo! El número era {numero_secreto}.")
            break

        if numero < numero_secreto:
            print(f"Demasiado bajo. Tiempo restante: {int(tiempo_restante)} segundos.\n")
        elif numero > numero_secreto:
            print(f"Demasiado alto. Tiempo restante: {int(tiempo_restante)} segundos.\n")
        else:
            print(f"🎉 ¡Correcto! Adivinaste el número en {intentos} intento(s) y en {int(tiempo_restante)} segundos.")
            break

def mensaje_despedida():
    print("\n¡Gran trabajo! ¡Nos vemos en el siguiente desafío!")