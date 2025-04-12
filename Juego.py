# juego_caliente_frio.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("¡Bienvenido! Adivina el número que estoy pensando entre 1 y 10.")
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos = 0

    while True:
        intento = input("¿Cuál es tu número?: ")

        if not intento.isdigit():
            print("Entrada inválida. Escribe un número por favor.")
            continue

        numero = int(intento)
        intentos += 1
        diferencia = abs(numero - numero_secreto)

        if numero == numero_secreto:
            print(f"🎉 ¡Increíble! Adivinaste el número en {intentos} intento(s).")
            break
        else:
            if diferencia <= 2:
                print("🔥 ¡Caliente! Estás muy cerca.\n")
            elif diferencia <= 5:
                print("🌡️ Tibio, sigue intentando.\n")
            else:
                print("❄️ Frío, estás lejos.\n")

def mensaje_despedida():
    print("\n¡Eso fue divertido! ¡Nos vemos en otro juego!")