# juego_con_puntuacion.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("🏆 ¡Bienvenido al juego con puntuación!")

    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos = 0
    puntos = 100  # Empieza con 100 puntos

    print(f"\nTienes que adivinar el número entre 1 y 10. Cada fallo hará que pierdas puntos.")

    while True:
        intento = input("Tu número: ")

        if not intento.isdigit():
            print("Eso no es un número válido. Intenta de nuevo.\n")
            continue

        numero_adivinado = int(intento)
        intentos += 1

        if numero_adivinado == numero_secreto:
            print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            print(f"Tu puntuación final es: {puntos} puntos.")
            break
        else:
            print(f"Intento {intentos}: No es el número secreto.")
            puntos -= 10  # Pierde 10 puntos por cada intento fallido
            print(f"Puntuación actual: {puntos} puntos.\n")
            
            if puntos <= 0:
                print("\n❌ ¡Te quedaste sin puntos! El juego ha terminado.")
                break

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Nos vemos en el siguiente desafío!")