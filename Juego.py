# juego_con_intentos_limitados.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("🎯 ¡Bienvenido al desafío de adivinar el número!")
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos_maximos = 5
    intentos = 0

    print(f"Estoy pensando en un número entre 1 y 10. Tienes {intentos_maximos} intentos para adivinarlo.\n")

    while intentos < intentos_maximos:
        respuesta = input("Tu número: ")

        if not respuesta.isdigit():
            print("Por favor, escribe un número válido.\n")
            continue

        numero = int(respuesta)
        intentos += 1

        if numero < numero_secreto:
            print("Muy bajo.\n")
        elif numero > numero_secreto:
            print("Muy alto.\n")
        else:
            print(f"🎉 ¡Correcto! Adivinaste el número en {intentos} intento(s).")
            break
    else:
        print(f"❌ Se acabaron los intentos. El número correcto era {numero_secreto}.")

    mensaje_despedida()

def mensaje_despedida():
    print("\nGracias por jugar. ¡Vuelve pronto!")