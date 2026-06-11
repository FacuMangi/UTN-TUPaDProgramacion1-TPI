# funcion que devuelve lista de diccionarios de paises que cuyo nombre coincide
# parcial o totalmente
def buscarPorNombre(paises: list, nombre: str):
    nombre = nombre.title()
    resultados = []

    for pais in paises:
        if nombre in pais["nombre"].title():
            resultados.append(pais)
    return resultados

# funcion que devuelve lista de diccionarios de paises de un continente especifico
def filtrarPorContinente(paises: list, continente: str):
    filtrados = []
    for pais in paises:
        if pais['continente'].title() == continente.title():
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una poblacion en un 
# rango especifico
def filtrarPorPoblacion(paises: list, minPob: int, maxPob: int):
    filtrados = []
    
    if minPob > maxPob:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = pais['poblacion']
        if minPob <= pob <= maxPob:
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una superficie en un 
# rango especifico
def filtrarPorSuperficie(paises: list, minSup: int, maxSup: int):
    filtrados = []
    
    if minSup > maxSup:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = pais['superficie']
        if minSup <= pob <= maxSup:
            filtrados.append(pais)
    return(filtrados)

# funcion que devuelve lista de diccionarios ordenados por pais
# utilizo una funcion anonima para pasar el valor de nombre de cada pais
# al parametro key de la funcion sorted
def ordenarPorNombre(paises: list):
    paisesOrdenados = sorted(paises, key=lambda x: x["nombre"])
    return(paisesOrdenados)

# funcion que devuelve lista de diccionarios ordenados por poblacion (asc)
def ordenarPorPoblacion(paises: list):
    paisesOrdenados = sorted(paises, key=lambda x: x["poblacion"])
    return(paisesOrdenados)

# funciones que devuelve lista de diccionarios ordenados por superficie (asc y desc)
def ordenarPorSuperficieAsc(paises: list):
    paisesOrdenados = sorted(paises, key=lambda x: x["superficie"])
    return(paisesOrdenados)

def ordenarPorSuperficieDesc(paises: list):
    paisesOrdenados = sorted(paises, reverse = True, key=lambda x: x["superficie"])
    return(paisesOrdenados)

# funcion que muestra pais con mayor poblacion
def mostrarMayorPobla(paises: list):
    mayorPobla = max(paises, key=lambda x: x["poblacion"])
    return(mayorPobla)

# funcion que muestra pais con menor poblacion
def mostrarMenorPobla(paises: list):
    menorPobla = min(paises, key=lambda x: x["poblacion"])
    return(menorPobla)

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
    cantPaises = 0
    for pais in paises:
        if pais["continente"].title() == continente.title():
            cantPaises += 1
    
    return(cantPaises)

# funcion que muestra los datos de un pais dado su diccionario
def mostrarPais(pais):
    print("\n------------------------")
    print(f"País: {pais['nombre']}")
    print(f"Población: {pais['poblacion']}")
    print(f"Superficie: {pais['superficie']} km²")
    print(f"Continente: {pais['continente']}")