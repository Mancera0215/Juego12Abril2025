# juego_con_rango_dinamico.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("🎯 ¡Bienvenido al juego de adivinanza con rango dinámico!")
    
    # Definir el rango inicial
    rango_min = 1
    rango_max = 10
    numero_secreto = generar_numero_aleatorio(rango_min, rango_max)
    intentos = 0

    print(f"\nEstoy pensando en un número entre {rango_min} y {rango_max}. ¡Adivina cuál es!")

    while True:
        intento = input("Tu número: ")

        if not intento.isdigit():
            print("Eso no es un número válido. Intenta de nuevo.\n")
            continue

        numero_adivinado = int(intento)
        intentos += 1

        if numero_adivinado == numero_secreto:
            print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            break
        else:
            if numero_adivinado < numero_secreto:
                print(f"Demasiado bajo. Rango actual: {rango_min} - {rango_max}")
            elif numero_adivinado > numero_secreto:
                print(f"Demasiado alto. Rango actual: {rango_min} - {rango_max}")
        
        # Reducir el rango después de cada intento fallido
        if intentos == 3:
            print("\n⚠️ ¡Primer fallo! El rango se reducirá.")
            rango_max = (rango_min + rango_max) // 2
        elif intentos == 5:
            print("\n⚠️ ¡Segundo fallo! El rango se reduce más aún.")
            rango_min = (rango_min + rango_max) // 2

        numero_secreto = generar_numero_aleatorio(rango_min, rango_max)  # Generar nuevo número dentro del nuevo rango

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Nos vemos en la próxima!")