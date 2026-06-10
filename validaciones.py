def inputNoVacio(mensaje):
	# Pide una cadena no vacía al usuario; vuelve a solicitar hasta
	# que reciba una entrada con algún carácter distinto de espacio.
	while True:
		v = input(mensaje).strip()
		if v:
			return v
		print("Entrada vacía. Intente de nuevo.")
		
def inputInt(mensaje, minimum=None, maximum=None):
	# Pide un entero al usuario con reintentos y validación opcional
	# de rango (minimum y maximum). Maneja ValueError internamente.
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