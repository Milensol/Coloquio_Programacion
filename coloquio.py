def total_puntos(archivo):
    pilotos_puntos = []
    i = 0
    for linea in archivo:
        # if i == 1: 
        #     break
        # i = i + 1
        
        piloto = linea[0:12].strip()
        equipo = linea[12:52].strip()
        puntos = linea[52:].strip().split()

        
        suma_puntos = 0
        for punto in puntos:
            try:
                valor = int(punto)
                suma_puntos += valor
            except ValueError:
                print(f"  Error al procesar el valor de puntos: {punto}")

        pilotos_puntos.append((piloto, suma_puntos))

    for i in range(len(pilotos_puntos)):
        for j in range(0, len(pilotos_puntos) - i - 1):
            if pilotos_puntos[j][1] < pilotos_puntos[j + 1][1]: 
                pilotos_puntos[j], pilotos_puntos[j + 1] = pilotos_puntos[j + 1], pilotos_puntos[j]

    print("\nListado de pilotos con sus puntos (de mayor a menor):\n")
    for piloto, puntos_totales in pilotos_puntos:
        print(f"{piloto}: {puntos_totales} puntos")
        print("-------------------------------------------")













#MENU
while True:
    opc= int(input("""\n             *********MENU*********
    1. Listado total de puntos de cada piloto, de mayor a menor puntaje.
    0. Si desea salir ingrese (0).
    Ingrese una opcion: """))
    with open("archivo.txt", "r") as archivo:
        next(archivo)
        if opc == 0: 
            break
        elif opc == 1:
            total_puntos(archivo)
