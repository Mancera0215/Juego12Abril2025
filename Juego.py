# juego_con_pistas_para_otro_jugador.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("👥 ¡Bienvenidos al juego de adivinanza con pistas para otro jugador!")
    
    # El jugador que pone el número
    numero_secreto = int(input("Jugador 1: Ingresa el número secreto (entre 1 y 10): "))
    while numero_secreto < 1 or numero_secreto > 10:
        print("Número fuera del rango permitido. Elige un número entre 1 y 10.")
        numero_secreto = int(input("Jugador 1: Ingresa el número secreto (entre 1 y 10): "))
    
    # El jugador que adivina
    print("\nJugador 2, tu tarea es adivinar el número secreto.")
    
    intentos = 0
    pistas = ["El número es impar", "El número es mayor que 5", "El número es menor que 8"]

    while True:
        intento = input("Tu intento: ")

        if not intento.isdigit():
            print("Eso no es un número válido. Intenta de nuevo.\n")
            continue
        
        numero_adivinado = int(intento)
        intentos += 1
        
        if numero_adivinado == numero_secreto:
            print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            break
        else:
            print(f"Intento {intentos}: No es el número secreto.")
            
            # Aquí el jugador 1 da una pista
            if intentos <= len(pistas):
                print(f"💡 Pista: {pistas[intentos - 1]}")
            else:
                print("💡 Pista: Sigue intentando, estás cerca.")
    
    mensaje_despedida()

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Nos vemos en la próxima!")