import csv
from validaciones import validarInputNumero, validarInputTexto

# funcion que toma lista de paises y diccionario de pais, agrega este ultimo a la lista
def agregarPais(paises: list):
    para_agregar = {}

    para_agregar["nombre"] = validarInputTexto("Ingrese nombre del pais: ").title()
    para_agregar["poblacion"] = validarInputNumero("Ingrese poblacion del pais: ")
    para_agregar["superficie"] = validarInputNumero("Ingrese superficie del pais: ")
    para_agregar["continente"] = validarInputTexto("Ingrese continente del pais: ").title()
    
    paises.append(para_agregar)

    return(paises)

def actualizarPobla():
    pass

def actualizarSuper():
    pass

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