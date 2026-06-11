import csv
from validaciones import validarInputNumero, validarInputTexto

# funcion que toma lista de paises y diccionario de pais, agrega este ultimo a la lista
def agregarPais(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    paraAgregar = {}

    nombre = validarInputTexto("Ingrese nombre del pais: ").title()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            raise ValueError(f"Error: {nombre} ya fue agregado previamente.")

    paraAgregar["nombre"] = nombre
    paraAgregar["poblacion"] = validarInputNumero(f"Ingrese poblacion para {nombre}: ")
    paraAgregar["superficie"] = validarInputNumero(f"Ingrese superficie para {nombre}: ")
    paraAgregar["continente"] = validarInputTexto(f"Ingrese continente para {nombre}: ").title()
    
    paises.append(paraAgregar)

    return(paises)

def actualizarPobla(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    pais = validarInputTexto("Ingresar pais para modificar poblacion: ")
    nuevaPobla = validarInputNumero(f"Ingresar nueva poblacion de {pais.title()}: ")

    actualizado = False

    for p in paises:
        if p["nombre"].lower() == pais.lower():
            p["poblacion"] = nuevaPobla
            actualizado = True
            break

    if not actualizado:
        raise ValueError(f'Error: no se encontro el pais "{pais}".')
    
    return(paises)

def actualizarSuper(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
    
    pais = validarInputTexto("Ingresar pais para modificar superficie: ")
    nuevaSuper = validarInputNumero(f"Ingresar nueva superficie de {pais.title()}: ")

    actualizado = False

    for p in paises:
        if p["nombre"].lower() == pais.lower():
            p["superficie"] = nuevaSuper
            actualizado = True
            break
    
    if not actualizado:
        raise ValueError(f'Error: no se encontro el pais "{pais}".')
    
    return(paises)

# funcion que devuelve filas de csv como lista de diccionarios con dupla key-value
def cargarPaises():
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        listaDic = list(csv.DictReader(archivo))
        
        # se convierten valores numericos de string a int
        for pais in listaDic:
            pais["poblacion"] = int(pais["poblacion"])
            pais["superficie"] = int(pais["superficie"])

        return(listaDic)

# funcion que toma lista de diccionarios y modifica csv con sus datos
def guardarCambios(paises: list):
    if not paises:
        raise ValueError("Error: no hay paises cargados.")
        
    columnas = ["nombre", "poblacion", "superficie", "continente"]

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
        escritorDict = csv.DictWriter(archivo, fieldnames=columnas)
        escritorDict.writeheader()
        escritorDict.writerows(paises)
