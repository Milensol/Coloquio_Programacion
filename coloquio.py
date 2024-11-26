def total_puntos(archivo):
    
    i = 0
    for linea in archivo:
        # if i == 1: 
        #     break
        # i = i + 1
        
        piloto = linea[0:12].strip()
        equipo = linea[12:52].strip()
        puntos = linea[52:].strip().split()

        print(f"Piloto: {piloto}")
        print(f"Equipo: {equipo}")

        suma_puntos = 0
        for punto in puntos:
            try:
                valor = int(punto)
                suma_puntos += valor
            except ValueError:
                print(f"  Error al procesar el valor de puntos: {punto}")

        print(f"Suma total de puntos: {suma_puntos}")
        print("-------------------------------------------")













#MENU
while True:
    opc= int(input("""             *********MENU*********
    1. Listado total de puntos de cada piloto, de mayor a menor puntaje.
    0. Si desea salir ingrese (0).
    Ingrese una opcion: """))
    with open("archivo.txt", "r") as archivo:
        next(archivo)
        if opc == 0: 
            break
        elif opc == 1:
            total_puntos(archivo)
