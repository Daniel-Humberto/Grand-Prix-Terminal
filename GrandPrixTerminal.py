import os
import sys
import time
import random




    # Funcion para limpiar la pantalla, utiliza 'cls' en Windows y 'clear' en sistemas Unix.
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')




    # Funcion para obtener las dimenciones actuales de la terminal
def obtener_dimensiones_terminal():
    try:
        columnas = os.get_terminal_size().columns
        filas = os.get_terminal_size().lines
    except:
        columnas = 75  # valor por defecto
        filas = 25     # valor por defecto
    return filas, columnas




    # Funcion para mostar la intro que incluye un logo ASCII, animación de carro y cuenta regresiva.
def mostrar_intro():


    filas, columnas = obtener_dimensiones_terminal()


    # Logo inicial
    logo = [
        "██████╗  ██████╗  █████╗ ███╗   ██╗██████╗     ██████╗ ██████╗ ██╗██╗  ██╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     ",
        "██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗    ██╔══██╗██╔══██╗██║╚██╗██╔╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     ",
        "██║  ███╗██████╔╝███████║██╔██╗ ██║██║  ██║    ██████╔╝██████╔╝██║ ╚███╔╝        ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     ",
        "██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║  ██║    ██╔═══╝ ██╔══██╗██║ ██╔██╗        ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     ",
        "╚██████╔╝██║  ██║██║  ██║██║ ╚████║██████╔╝    ██║     ██║  ██║██║██╔╝ ██╗       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗",
        " ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝"
    ]


    # Animación de carro moviéndose
    carro = [
        "  ______",
        " /|_||_\\`.__",
        "(   _    _ _\\",
        "=`-(_)--(_)-' "
    ]


    # Animación de cuenta regresiva
    numeros = {
        "3": [
            "███████╗",
            "╚════██║",
            "  █████║",
            "  ╚══██║",
            "███████║",
            "╚══════╝"
        ],
        "2": [
            " ██████╗ ",
            "██╔═══██╗",
            "    ██╔╝",
            "  ██╔╝ ",
            "██╔╝  ",
            "███████╗ ",
            "╚══════╝ "
        ],
        "1": [
            " ██╗",
            "███║",
            "╚██║",
            " ██║",
            " ██║",
            " ╚═╝"
        ],
        "GO": [
            "  ██████╗  ██████╗ ██╗",
            " ██╔════╝ ██╔═══██╗██║",
            " ██║  ███╗██║   ██║██║",
            " ██║   ██║██║   ██║╚═╝",
            " ╚██████╔╝╚██████╔╝██╗",
            "  ╚═════╝  ╚═════╝ ╚═╝"
        ]
    }


    # Efecto de aparición gradual del logo
    limpiar_pantalla()
    for i in range(len(logo[0])):
        limpiar_pantalla()
        for linea in logo:
            print(linea[:i].center(columnas))
        time.sleep(0.01)
    time.sleep(1)


    # Efecto para la animación del carro atravesando la pantalla
    for pos in range(-10, columnas, 2):
        limpiar_pantalla()
        for linea in logo:
            print(linea.center(columnas))
        print("\n" * 2)
        for linea in carro:
            print((" " * pos + linea).center(columnas))
        time.sleep(0.01)


    # Efecto para cuenta regresiva
    for numero in ["3", "2", "1", "GO"]:
        limpiar_pantalla()
        espacio_vertical = (filas - len(numeros[numero])) // 2
        print("\n" * espacio_vertical)
        for linea in numeros[numero]:
            print(linea.center(columnas))
        time.sleep(1)


    limpiar_pantalla()




    # Funcion principal que ejecuta la carrera, gestiona los coches, y determina el ganador                                                                                                                                                                                                                                                                                                                                                                                                                                                             
def ejecutar_carrera():
    # Definir los autos con sus nombres y arte ASCII
    coches = {
        "Auto Rojo": [
            "      ______",
            "     /|_||_\\`.__",
            "    (   _    _ _\\",
            "    =`-(_)--(_)-' "
        ],
        "Camión Azul": [
            "      ______",
            "     /|_||_\\`.__",
            "    (   _    _ _\\",
            "    =`-(_)--(_)-' "
        ],
        "Camión Verde": [
            "      ______",
            "     /|_||_\\`.__",
            "    (   _    _ _\\",
            "    =`-(_)--(_)-' "
        ],
        "Camión Amarillo": [
            "      ______",
            "     /|_||_\\`.__",
            "    (   _    _ _\\",
            "    =`-(_)--(_)-' "
        ],
    }

    # Distancia total de la carrera
    distancia_meta = 150
    progreso = {coche: 0 for coche in coches}


        # Función que actualiza y muestra el estado de la carrera al visualizar la posición de cada vehículo en la pista.
    def mostrar_carrera():
        limpiar_pantalla()
        print("\n" + "-" * (distancia_meta + 20))
        for coche, arte in coches.items():
            distancia = progreso[coche]
            espacio = " " * distancia
            print(f"{coche}:")
            for linea in arte:
                print(f"{espacio}{linea}")
            print()
        print("-" * (distancia_meta + 20))


    print("¡Inicia el Grand Prix en Terminal!")
    time.sleep(1)
    

    while max(progreso.values()) < distancia_meta:
        for coche in coches:
            progreso[coche] += random.randint(1, 3)
            if progreso[coche] > distancia_meta:
                progreso[coche] = distancia_meta


        mostrar_carrera()
        time.sleep(0.1)


    # Determinar ganador
    ganador = max(progreso, key=progreso.get)
    return ganador




    # Funcion para mostrar banner segun ganador
def mostrar_pantalla_ganador(ganador):
    limpiar_pantalla()
    filas, columnas = obtener_dimensiones_terminal()
    

    # Trophy ASCII Art
    trofeo = [
        "   ___________     ",
        "  '._==_==_=_.'    ",
        " .-\\         /-.   ",
        "| (|:.       |) |  ",
        " '-|:.       |-'   ",
        "   \\::.     /      ",
        "     '::. .'       ",
        "       ) (         ",
        "     _.' '._       ",
        "    '-------'      ",
    ]


    # Banner Winner
    banner = [
        "██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ ██╗",
        "██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗██║",
        "██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝██║",
        "██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗╚═╝",
        "╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║██╗",
        " ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝"
    ]


    # Efectos de confeti
    confeti = ["*", "•", "○", "★", "☆", "✦", "✧", "⋆", "✯", "✮"]


    # Mostrar banner con efecto
    for i in range(len(banner[0])):
        limpiar_pantalla()
        for linea in banner:
            print(linea[:i].center(columnas))
        time.sleep(0.015)


    print("\n")


    # Mostrar trofeo
    for linea in trofeo:
        print(linea.center(columnas))
        time.sleep(0.15)


    # Mostrar nombre del ganador
    nombre_ganador = [
        f"╔{'═' * (len(ganador) + 8)}╗",
        f"║   {ganador}   ║",
        f"╚{'═' * (len(ganador) + 8)}╝"
    ]
    print("\n")
    for linea in nombre_ganador:
        print(linea.center(columnas))
        time.sleep(0.25)


    # Efecto de confeti cayendo
    for _ in range(10):    # 10 oleadas de confeti
        limpiar_pantalla()
        
        # Mantener el banner y trofeo
        for linea in banner:
            print(linea.center(columnas))
        print("\n")
        for linea in trofeo:
            print(linea.center(columnas))
        print("\n")
        for linea in nombre_ganador:
            print(linea.center(columnas))


        # Agregar confeti aleatorio
        for _ in range(20):
            pos_x = random.randint(0, columnas-1)
            pos_y = random.randint(0, filas-1)
            print(f"\033[{pos_y};{pos_x}H{random.choice(confeti)}", end='', flush=True)
        
        time.sleep(0.5)


    # Mensaje final y opciones
    print("\n\n")
    mensaje_final = "¡FELICITACIONES POR TU VICTORIA EN EL GRAND PRIX TERMINAL!"
    print(mensaje_final.center(columnas))
    print("\n")


    # Mostrar opciones y obtener input del usuario
    opciones = "[1] Nueva Carrera   [2] Salir"
    print(opciones.center(columnas))
    print("\n")


    while True:
        try:
            opcion = input("Selecciona una opción (1 o 2): ".center(columnas))
            if opcion in ['1', '2']:
                return opcion
            else:
                print("Por favor, selecciona 1 o 2.".center(columnas))
        except KeyboardInterrupt:
            return '2'




    # Funcion principal, ejecuta la carrera, muestra el ganador, y gestiona la opción de salir o continuar
def main():
    while True:
        mostrar_intro()
        ganador = ejecutar_carrera()
        opcion = mostrar_pantalla_ganador(ganador)
        
        if opcion == '2':
            limpiar_pantalla()
            print("\n¡Gracias por jugar al Grand Prix Terminal! ¡Hasta la próxima!")
            time.sleep(2)
            sys.exit(0)
        
        limpiar_pantalla()




    # Ejecuta la función principal y maneja la interrupción por el usuario.
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nJuego interrumpido por el usuario. ¡Hasta luego!")
        sys.exit(0)