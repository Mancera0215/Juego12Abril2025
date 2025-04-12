# juego_con_superpoderes.py
from utils import generar_numero_aleatorio

def iniciar_juego():
    print("⚡ ¡Bienvenido al juego con superpoderes!")
    
    numero_secreto = generar_numero_aleatorio(1, 10)
    intentos = 0
    intentos_maximos = 5
    superpoder_usado = False

    print(f"\nTienes {intentos_maximos} intentos para adivinar el número entre 1 y 10. Usa tus superpoderes sabiamente.")

    while intentos < intentos_maximos:
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
            print(f"Intento {intentos}: No es el número secreto.")
        
            # Si el jugador no ha usado el superpoder, le preguntamos si quiere usarlo
            if not superpoder_usado:
                usar_superpoder = input("¿Quieres usar tu superpoder? (sí/no): ").lower()
                if usar_superpoder == 'sí':
                    superpoder_usado = True
                    print("🔮 ¡Usaste el superpoder!")
                    superpoder()
                
            if intentos == intentos_maximos:
                print(f"\n❌ Se acabaron los intentos. El número secreto era {numero_secreto}.")
                break

def superpoder():
    print("\n¡Tienes un superpoder disponible! Estas son tus opciones:")
    print("1. Obtener una pista sobre el número secreto.")
    print("2. Obtener un intento adicional.")
    print("3. Cambiar el rango del número secreto.")
    
    opcion = input("Elige tu superpoder (1/2/3): ")

    if opcion == '1':
        print("💡 Pista: El número es impar." if generar_numero_aleatorio(1, 10) % 2 == 1 else "💡 Pista: El número es par.")
    elif opcion == '2':
        print("🎉 ¡Has obtenido un intento adicional!")
        global intentos_maximos
        intentos_maximos += 1
    elif opcion == '3':
        print("🔄 El rango se ha cambiado de 1-10 a 1-5.")
        global numero_secreto
        numero_secreto = generar_numero_aleatorio(1, 5)
    else:
        print("Opción no válida, intenta de nuevo.")

def mensaje_despedida():
    print("\n¡Gracias por jugar! ¡Nos vemos en la próxima aventura con superpoderes!")