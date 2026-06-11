# funcion que devuelve lista de diccionarios de paises que cuyo nombre coincide
# parcial o totalmente
def buscarPorNombre(paises: list, nombre: str):
    nombre = nombre.lower()
    resultados = []

    for pais in paises:
        if nombre in pais["nombre"].lower():
            resultados.append(pais)
    return resultados

# funcion que devuelve lista de diccionarios de paises de un continente especifico
def filtrarPorContinente(paises: list, continente: str):
    filtrados = []
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una poblacion en un 
# rango especifico
def filtrarPorPoblacion(paises: list, min_pob: int, max_pob: int):
    filtrados = []
    
    if min_pob > max_pob:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = pais['poblacion']
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
        pob = pais['superficie']
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
    paises_ordenados = sorted(paises, key=lambda x: x["poblacion"])
    return(paises_ordenados)

# funciones que devuelve lista de diccionarios ordenados por superficie (asc y desc)
def ordenarPorSuperficieAsc(paises: list):
    paises_ordenados = sorted(paises, key=lambda x: x["superficie"])
    return(paises_ordenados)

def ordenarPorSuperficieDesc(paises: list):
    paises_ordenados = sorted(paises, reverse = True, key=lambda x: x["superficie"])
    return(paises_ordenados)

# funcion que muestra pais con mayor poblacion
def mostrarMayorPobla(paises: list):
    mayor_pobla = max(paises, key=lambda x: x["poblacion"])
    return(mayor_pobla)

# funcion que muestra pais con menor poblacion
def mostrarMenorPobla(paises: list):
    menor_pobla = min(paises, key=lambda x: x["poblacion"])
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
        sumaSuper += pais["superficie"]
    promedio = sumaSuper//len(paises)
    return(promedio)

# funcion que devuelve integer cantidad de paises por continente
def mostrarCantPorCont(paises: list, continente: str):
    cant_paises = 0
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            cant_paises += 1
    
    return(cant_paises)

# funcion que muestra los datos de un pais dado su diccionario
def mostrarPais(pais):
    print("\n------------------------")
    print(f"País: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")