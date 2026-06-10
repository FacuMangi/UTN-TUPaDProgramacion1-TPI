import csv

# Hay que modificarla para que tome LISTA DE DICCIONARIOS y le de formato a los datos en consola
# funcion que devuelve array de lineas del csv
def mostrarPaises():
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector)
        print(f"{encabezados[0]} | {encabezados[1]} | {encabezados[2]} | {encabezados[3]}")

        for fila in lector:
            # cada fila es una lista, ej: [Australia,27000000,7692024,Oceania]
            pais = fila[0]
            poblacion = fila[1]
            superficie = fila[2]
            continente = fila[3]

            print(f"{pais} | {poblacion} | {superficie} | {continente}")

# funcion que devuelve filas de csv como lista de diccionarios con dupla key-value
def cargarPaises():
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        listaDic = list(csv.DictReader(archivo))
        return(listaDic)

# funcion que devuelve lista de diccionarios de paises de un continente especifico
def filtrarPorContinente(paises: list, continente: str):
    filtrados = []
    for pais in paises:
        if pais['continente'] == continente:
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una poblacion en un 
# rango especifico
def filtrarPorPoblacion(paises: list, min_pob: int, max_pob: int):
    filtrados = []
    
    if min_pob > max_pob:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = int(pais['poblacion'])
        if min_pob <= pob <= max_pob:
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una superficie en un 
# rango especifico
def filtrarPorSuperficie(paises: list, min_sup: int, max_sup: int):
    filtrados = []
    
    if min_sup > max_sup:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = int(pais['superficie'])
        if min_sup <= pob <= max_sup:
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios ordenados por pais
# utilizo una funcion anonima para pasar el valor de nombre de cada pais
# al parametro key de la funcion sorted
def ordenarPorNombre(paises: list):
    paises_ordenados = sorted(paises, key=lambda x: x["nombre"])
    return(paises_ordenados)

# funcion que devuelve lista de diccionarios ordenados por poblacion (asc)
def ordenarPorPoblacion(paises: list):
    paises_ordenados = sorted(paises, key=lambda x: int(x["poblacion"]))
    return(paises_ordenados)

# funciones que devuelve lista de diccionarios ordenados por superficie (asc y desc)
def ordenarPorSuperficieAsc(paises: list):
    paises_ordenados = sorted(paises, key=lambda x: int(x["superficie"]))
    return(paises_ordenados)

def ordenarPorSuperficieDesc(paises: list):
    paises_ordenados = sorted(paises, reverse = False, key=lambda x: int(x["superficie"]))
    return(paises_ordenados)

# funcion que muestra pais con mayor poblacion
def mostrarMayorPobla(paises: list):
    mayor_pobla = max(paises, key=lambda x: int(x["poblacion"]))
    return(mayor_pobla)

# funcion que muestra pais con menor poblacion
def mostrarMenorPobla(paises: list):
    menor_pobla = min(paises, key=lambda x: int(x["poblacion"]))
    return(menor_pobla)

# funcion que muestra el promedio de la poblacion de todos los paises
def mostrarPromedioPobla(paises: list):
    sumaPobla = 0
    for pais in paises:
        sumaPobla += int(pais["poblacion"])
    promedio = sumaPobla//len(paises)
    return(promedio)

# funcion que muestra el promedio de la superficie de todos los paises
def mostrarPromedioSuper(paises: list):
    sumaSuper = 0
    for pais in paises:
        sumaSuper += int(pais["superficie"])
    promedio = sumaSuper//len(paises)
    return(promedio)

def mostrarCantPorCont(paises: list, continente: str):
    cant_paises = 0
    for pais in paises:
        if pais["continente"] == continente:
            cant_paises += 1
    
    return(cant_paises)

print(mostrarCantPorCont(cargarPaises(), "Oceania"))