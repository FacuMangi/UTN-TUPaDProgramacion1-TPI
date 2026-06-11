# funcion que devuelve lista de diccionarios de paises que cuyo nombre coincide
# parcial o totalmente
def buscarPorNombre(paises: list, nombre: str):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    nombre = nombre.lower()
    resultados = []

    for pais in paises:
        if nombre in pais["nombre"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        raise ValueError("No se encontraron paises con ese nombre.")
    
    return resultados

# funcion que devuelve lista de diccionarios de paises de un continente especifico
def filtrarPorContinente(paises: list, continente: str):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    filtrados = []

    for pais in paises:
        if continente.lower() in pais['continente'].lower():
            filtrados.append(pais)

    if len(filtrados) == 0:
        raise ValueError("No se encontraron paises para el continente ingresado.")
    
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una poblacion en un 
# rango especifico
def filtrarPorPoblacion(paises: list, minPob: int, maxPob: int):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    filtrados = []
    
    if minPob > maxPob:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = pais['poblacion']
        if minPob <= pob <= maxPob:
            filtrados.append(pais)

    if len(filtrados) == 0:
        raise ValueError("No se encontraron paises para el rango ingresado.")
                
    return(filtrados)

# funcion que devuelve lista de diccionarios de paises con una superficie en un 
# rango especifico
def filtrarPorSuperficie(paises: list, minSup: int, maxSup: int):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    filtrados = []
    
    if minSup > maxSup:
        raise ValueError("Error: minimo es mayor que maximo.")
    
    for pais in paises:
        pob = pais['superficie']
        if minSup <= pob <= maxSup:
            filtrados.append(pais)

    if len(filtrados) == 0:
        raise ValueError("No se encontraron paises para el rango ingresado.")

    return(filtrados)

# funcion que devuelve lista de diccionarios ordenados por pais
# utilizo una funcion anonima para pasar el valor de nombre de cada pais
# al parametro key de la funcion sorted
def ordenarPorNombre(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    paisesOrdenados = sorted(paises, key=lambda x: x["nombre"])
    return(paisesOrdenados)

# funcion que devuelve lista de diccionarios ordenados por poblacion (asc)
def ordenarPorPoblacion(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    paisesOrdenados = sorted(paises, key=lambda x: x["poblacion"])
    return(paisesOrdenados)

# funciones que devuelve lista de diccionarios ordenados por superficie (asc y desc)
def ordenarPorSuperficieAsc(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    paisesOrdenados = sorted(paises, key=lambda x: x["superficie"])
    return(paisesOrdenados)

def ordenarPorSuperficieDesc(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    paisesOrdenados = sorted(paises, reverse = True, key=lambda x: x["superficie"])
    return(paisesOrdenados)

# funcion que muestra pais con mayor poblacion
def mostrarMayorPobla(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    mayorPobla = max(paises, key=lambda x: x["poblacion"])
    return(mayorPobla)

# funcion que muestra pais con menor poblacion
def mostrarMenorPobla(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    menorPobla = min(paises, key=lambda x: x["poblacion"])
    return(menorPobla)

# funcion que muestra el promedio de la poblacion de todos los paises
def mostrarPromedioPobla(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
        
    sumaPobla = 0
    for pais in paises:
        sumaPobla += int(pais["poblacion"])

    promedio = round(sumaPobla / len(paises), 2)

    return(promedio)

# funcion que muestra el promedio de la superficie de todos los paises
def mostrarPromedioSuper(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    sumaSuper = 0
    for pais in paises:
        sumaSuper += pais["superficie"]

    promedio = round(sumaSuper / len(paises), 2)

    return(promedio)

# funcion que devuelve integer cantidad de paises por continente
def mostrarCantPorCont(paises: list, continente: str):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
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