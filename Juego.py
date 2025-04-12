# juego_con_pistas_estrategicas.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("🎯 ¡Bienvenido al juego de adivinar el número con pistas!")
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos = 0

    print(f"\nEstoy pensando en un número entre 1 y 10. ¡Adivina cuál es!")

    while True:
        intento = input("Tu número: ")

        if not intento.isdigit():
            print("Eso no es un número. Intenta de nuevo.\n")
            continue

        numero = int(intento)
        intentos += 1

        if numero < numero_secreto:
            print("Muy bajo.\n")
        elif numero > numero_secreto:
            print("Muy alto.\n")
        else:
            print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            break

        # Aquí se dan pistas cada cierto número de intentos
        if intentos == 3:
            print("💡 Pista: Estás cerca, el número está en el rango de 5-10.")
        elif intentos == 5:
            print("💡 Pista: El número es mayor que 7.")
        elif intentos == 7:
            print("💡 Pista final: El número es menor que 9.")

def mensaje_despedida():
    print("\nGracias por jugar. ¡Nos vemos en el siguiente desafío!")