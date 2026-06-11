import csv
from validaciones import validarInputNumero, validarInputTexto

# funcion que toma lista de paises y diccionario de pais, agrega este ultimo a la lista
def agregarPais(paises: list):
    paraAgregar = {}

    paraAgregar["nombre"] = validarInputTexto("Ingrese nombre del pais: ").title()
    paraAgregar["poblacion"] = validarInputNumero("Ingrese poblacion del pais: ")
    paraAgregar["superficie"] = validarInputNumero("Ingrese superficie del pais: ")
    paraAgregar["continente"] = validarInputTexto("Ingrese continente del pais: ").title()
    
    paises.append(paraAgregar)

    return(paises)

def actualizarPobla(paises: list):
    pais = validarInputTexto("Ingresar pais para modificar poblacion: ").title()
    nuevaPobla = validarInputNumero(f"Ingresar nueva poblacion de {pais}: ")

    for p in paises:
        if p["nombre"] == pais:
            p["poblacion"] = nuevaPobla
    
    return(paises)

def actualizarSuper(paises: list):
    pais = validarInputTexto("Ingresar pais para modificar superficie: ").title()
    nuevaSuper = validarInputNumero(f"Ingresar nueva superficie de {pais}: ")

    for p in paises:
        if p["nombre"] == pais:
            p["superficie"] = nuevaSuper
    
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
    with open("paises.csv", "w", encoding="utf-8") as archivo:
        pass