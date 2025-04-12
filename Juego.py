# juego_con_intentos_limitados.py
from utils import generar_numero_aleatorio

MAX_INTENTOS = 5

def iniciar_juego():
    print("🎯 ¡Bienvenido! Tienes 5 intentos para adivinar el número entre 1 y 10.")
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos_realizados = 0

    while intentos_realizados < MAX_INTENTOS:
        intento = input(f"Intento {intentos_realizados + 1} de {MAX_INTENTOS}: ")

        if not intento.isdigit():
            print("Por favor ingresa un número válido.")
            continue

        numero = int(intento)
        intentos_realizados += 1

        if numero < numero_secreto:
            print("Muy bajo.\n")
        elif numero > numero_secreto:
            print("Muy alto.\n")
        else:
            print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos_realizados} intento(s).")
            break
    else:
        print(f"😔 ¡Se acabaron los intentos! El número correcto era {numero_secreto}.")

    mensaje_despedida()

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Vuelve pronto!")