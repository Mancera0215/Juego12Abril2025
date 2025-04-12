# adivina_numero_limitado.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("¡Estoy pensando en un número entre 1 y 10!")
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos_restantes = 5

    while intentos_restantes > 0:
        intento = input(f"Te quedan {intentos_restantes} intento(s). Ingresa un número: ")

        if not intento.isdigit():
            print("Entrada inválida. Por favor, escribe un número.")
            continue

        numero = int(intento)

        if numero < numero_secreto:
            print("Demasiado pequeño.\n")
        elif numero > numero_secreto:
            print("Demasiado grande.\n")
        else:
            print(f"¡Bien hecho! Adivinaste el número en {5 - intentos_restantes + 1} intento(s).")
            break

        intentos_restantes -= 1

    else:
        print(f"\n¡Se acabaron los intentos! El número era {numero_secreto}.")

def mensaje_despedida():
    print("\nGracias por jugar. ¡Vuelve pronto!")