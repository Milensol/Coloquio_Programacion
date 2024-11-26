def total_puntos(archivo):
    pilotos_puntos = []
    i = 0
    for linea in archivo:
        
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< NO ENTENDI ESTO XD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # if i == 1: 
        #     break
        # i = i + 1
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
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

def total_puntos_equipos(archivo):
    equipos_puntos = {}

    for linea in archivo:
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

        # ACA SE ACUMULA LOS PUNTOS DE CADA EQUIPO
        if equipo not in equipos_puntos:
            equipos_puntos[equipo] = suma_puntos
        else:
            equipos_puntos[equipo] += suma_puntos

    # ACA SE ORDNEA DE MAYOR A MENOR 
    equipos_ordenados = list(equipos_puntos.items())
    for i in range(len(equipos_ordenados)):
        for j in range(0, len(equipos_ordenados) - i - 1):
            if equipos_ordenados[j][1] < equipos_ordenados[j + 1][1]:
                equipos_ordenados[j], equipos_ordenados[j + 1] = equipos_ordenados[j + 1], equipos_ordenados[j]

    print("\nListado de equipos con sus puntos (de mayor a menor):\n")
    for equipo, puntos_totales in equipos_ordenados:
        print(f"{equipo}: {puntos_totales} puntos")
        print("-------------------------------------------")
        
def promedio_puntos_pilotos(archivo):
    pilotos_puntos = {}
    
    for linea in archivo:
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

        # ACA SE GUARDA LOS PUNTOS Y CANTIDAD DE CARRERAS
        if piloto not in pilotos_puntos:
            pilotos_puntos[piloto] = {'total': suma_puntos, 'carreras': len(puntos)}
        else:
            pilotos_puntos[piloto]['total'] += suma_puntos
            pilotos_puntos[piloto]['carreras'] += len(puntos)

    # ACA SE CALCULA EL PROMEDIO DE LOS PILOTOS
    promedios = []
    for piloto, datos in pilotos_puntos.items():
        promedio = datos['total'] / datos['carreras']
        promedios.append((piloto, promedio))

    # ACA SE ORDENA LOS PROMEDIOS DE MAYOR A MENOR
    for i in range(len(promedios)):
        for j in range(0, len(promedios) - i - 1):
            if promedios[j][1] < promedios[j + 1][1]:
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]

    # ACA SE MUESTRA LOS PROMEDIOS ORDENADOS
    print("\nPromedio de puntos por piloto (de mayor a menor):\n")
    for piloto, promedio in promedios:
        print(f"{piloto}: {promedio:.2f} puntos promedio")
        print("-------------------------------------------")
        
        
        
#MENU
while True:
    opc= int(input("""\n             *********MENU*********
    1. Listado total de puntos de cada piloto (ORDENADO DE MAYOR A MENOR PUNTAJE).
    2. Listado de puntos de cada equipo (ORDENADO DE MAYOR A MENOR PUNTAJE).
    3. Promedio de puntos de cada piloto (ORDENADO DE MAYOR A MENOR PUNTAJE)
    4. Mejor posición obtenida por cada piloto (EN ORDEN ALFABÉTICO)
    0. Si desea salir ingrese (0).
    Ingrese una opcion: """))
    with open("archivo.txt", "r") as archivo:
        next(archivo) # SE SALTA EL ENCABEZADO
        if opc == 0: 
            break
        elif opc == 1:
            total_puntos(archivo)
        elif opc == 2:
            total_puntos_equipos(archivo)
        elif opc == 3:
            promedio_puntos_pilotos(archivo)
        else:
            print("OPCION INVALIDA. PRUEBE CON UNA CORRECTA")
print("MESSI")