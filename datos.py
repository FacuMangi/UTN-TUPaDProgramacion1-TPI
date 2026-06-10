import csv

def agregarPais():
    pass

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