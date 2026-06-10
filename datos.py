import csv

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
# utilizo una funcion anonima para pasar el valor de poblacion de cada pais
# al parametro key de la funcion sorted
def ordenarPorPoblacion(paises: list):
    paises_ordenados = sorted(paises, key=lambda x: int(x["poblacion"]))
    return(paises_ordenados)

# funciones que devuelve lista de diccionarios ordenados por superficie (asc y desc)
# utilizo una funcion anonima para pasar el valor de superficie de cada pais
# al parametro key de la funcion sorted
def ordenarPorSuperficieAsc(paises: list):
    paises_ordenados = sorted(paises, key=lambda x: int(x["superficie"]))
    return(paises_ordenados)

def ordenarPorSuperficieDesc(paises: list):
    paises_ordenados = sorted(paises, reverse = False, key=lambda x: int(x["superficie"]))
    return(paises_ordenados)

print(ordenarPorSuperficieDesc(cargarPaises()))