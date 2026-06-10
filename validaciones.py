# Funcion que recibe un mensaje que luego usa para crear un input
# luego valida ese input como string en un loop while
def validarTexto(mensaje: str):
	while True:
		v = input(mensaje).strip()
		if v and v.replace(" ", "").isalpha():
			return v
		print("Entrada vacía o no es texto valido. Intente de nuevo.")

# Funcion que recibe un mensaje que luego usa para crear un input
# luego valida ese input como integer en un loop while (devuelve string)
def validarNumero(mensaje: str):
	while True:
		s = input(mensaje).strip()
		if s == "":
			print("Entrada vacía. Intente de nuevo.")
			continue
		try:
			v = int(s)
		except ValueError:
			print("Entrada no es un número entero válido. Intente de nuevo.")
			continue
		if v <= 0:
			print("Ingrese un número positivo (mayor que 0).")
			continue
		return str(v)

# 
def inputInt(mensaje, minimum=None, maximum=None):
	while True:
		try:
			v = int(input(mensaje))
		except ValueError:
			print("Entrada inválida. Ingrese un número entero.")
			continue
		if minimum is not None and v < minimum:
			print(f"El número debe ser >= {minimum}.")
			continue
		if maximum is not None and v > maximum:
			print(f"El número debe ser <= {maximum}.")
			continue
		return v