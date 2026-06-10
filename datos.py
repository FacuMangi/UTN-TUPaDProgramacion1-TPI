import csv
from validaciones import validarNumero, validarTexto

# funcion que toma lista de paises y diccionario de pais, agrega este ultimo a la lista
def agregarPais(paises: list):
    para_agregar = {}

    para_agregar["nombre"] = validarTexto("Ingrese nombre del pais: ").title()
    para_agregar["poblacion"] = validarNumero("Ingrese poblacion del pais: ")
    para_agregar["superficie"] = validarNumero("Ingrese superficie del pais: ")
    para_agregar["continente"] = validarTexto("Ingrese continente del pais: ").title()
    
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
        return(listaDic)

# funcion que toma lista de diccionarios y modifica csv con sus datos
def guardarCambios(paises: list):
    with open("paises.csv", "w", encoding="utf-8") as archivo:
        pass