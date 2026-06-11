from datos import cargarPaises, guardarCambios, agregarPais, actualizarPobla, actualizarSuper
from busquedas import (buscarPorNombre, filtrarPorContinente, filtrarPorPoblacion, filtrarPorSuperficie, 
ordenarPorNombre, ordenarPorPoblacion, ordenarPorSuperficieAsc, ordenarPorSuperficieDesc, mostrarMayorPobla,
mostrarMenorPobla, mostrarPromedioPobla, mostrarPromedioSuper, mostrarCantPorCont, mostrarPais)
from validaciones import validarInputTexto, inputInt

# Menu principal del programa
def mostrarMenu():
    print("\n===== MENÚ =====")
    print("1. Buscar país por nombre")
    print("2. Filtrar países")
    print("3. Ordenar países")
    print("4. Mostrar estadísticas")
    print("5. Agregar país")
    print("6. Actualizar población")
    print("7. Actualizar superficie")
    print("8. Guardar cambios")
    print("0. Salir")

# Submenú de filtros
def menuFiltros():
    print("\n===== FILTRAR POR =====")
    print("1. Por continente")
    print("2. Por población")
    print("3. Por superficie")
    print("0. Volver al menú principal")

# Submenú de ordenamientos
def menuOrdenamiento():
    print("\n===== ORDENAR POR =====")
    print("1. Por nombre (A-Z)")
    print("2. Por población (menor a mayor)")
    print("3. Por superficie (menor a mayor)")
    print("4. Por superficie (mayor a menor)")
    print("0. Volver al menú principal")

# Submenú de estadísticas
def menuEstadisticas():
    print("\n===== ESTADÍSTICAS =====")
    print("1. País con mayor población")
    print("2. País con menor población")
    print("3. Promedio de población")
    print("4. Promedio de superficie")
    print("5. Cantidad de países por continente")
    print("0. Volver al menú principal")

def main():
    # Carga inicial de los datos desde el archivo CSV
    paises = cargarPaises()

    while True:
        mostrarMenu()
        opcion = inputInt("Seleccione una opción: ", 0, 8)

        # ==========================
        # BUSQUEDA DE PAÍSES
        # ==========================
        if opcion == 1:
            print("\n===== BUSCAR PAÍS =====")
            try:
                nombre = validarInputTexto("Ingrese el nombre del país a buscar: ")
                resultados = buscarPorNombre(paises, nombre)

                print(f"\n{len(resultados)} resultados con '{nombre}':")
                
                for pais in resultados:
                    mostrarPais(pais)

            except ValueError as e:
                print(f"\n{e}")
        # ==========================
        # FILTROS DE PAÍSES
        # ==========================
        elif opcion == 2:
            while True:
                menuFiltros()
                op_filtro = inputInt("Seleccione una opción: ", 0, 3)

                try:
                    if op_filtro == 1:
                        cont = validarInputTexto("Ingrese continente: ")
                        resultados = filtrarPorContinente(paises, cont)

                    elif op_filtro == 2:
                        pob_min = inputInt("Ingrese población mínima: ", 0, 10_000_000_000)
                        pob_max = inputInt("Ingrese población máxima: ", pob_min, 10_000_000_000)
                        resultados = filtrarPorPoblacion(paises, pob_min, pob_max)

                    elif op_filtro == 3:
                        sup_min = inputInt("Ingrese superficie mínima: ", 0, 20_000_000)
                        sup_max = inputInt("Ingrese superficie máxima: ", sup_min, 20_000_000)
                        resultados = filtrarPorSuperficie(paises, sup_min, sup_max)

                    elif op_filtro == 0:
                        break

                    # Muestra resultados
                    if op_filtro != 0:
                        print(f"\n{len(resultados)} países encontrados:")
                        for pais in resultados:
                            mostrarPais(pais)

                except ValueError as e:
                    print(f"\n{e}")

        # ==========================
        # ORDENAMIENTO DE PAÍSES
        # ==========================
        elif opcion == 3:
            while True:
                menuOrdenamiento()
                op_orden = inputInt("Seleccione una opción: ", 0, 4)

                try:
                    if op_orden == 1:
                        resultados = ordenarPorNombre(paises)

                    elif op_orden == 2:
                        resultados = ordenarPorPoblacion(paises)

                    elif op_orden == 3:
                        resultados = ordenarPorSuperficieAsc(paises)

                    elif op_orden == 4:
                        resultados = ordenarPorSuperficieDesc(paises)

                    elif op_orden == 0:
                        break

                    # Muestra resultados
                    if op_orden != 0:
                        print(f"\n{len(resultados)} países ordenados:")
                        for pais in resultados:
                            mostrarPais(pais)

                except ValueError as e:
                    print(f"\n{e}")

        # ==========================
        # ESTADÍSTICAS DE PAÍSES
        # ==========================
        elif opcion == 4:
            while True:
                menuEstadisticas()
                op_estad = inputInt("Seleccione una opción: ", 0, 5)

                try:
                    if op_estad == 1:
                        pais = mostrarMayorPobla(paises)
                        print("\nPaís con mayor población:")
                        mostrarPais(pais)
                    
                    elif op_estad == 2:
                        pais = mostrarMenorPobla(paises)
                        print("\nPaís con menor población:")
                        mostrarPais(pais)
                    
                    elif op_estad == 3:
                        promedio = mostrarPromedioPobla(paises)
                        print(f"\nPromedio de población: {promedio:,} habitantes")

                    elif op_estad == 4:
                        promedio = mostrarPromedioSuper(paises)
                        print(f"\nPromedio de superficie: {promedio:,} km²")

                    elif op_estad == 5:
                        continente = validarInputTexto("Ingrese continente: ")
                        cantidad = mostrarCantPorCont(paises, continente)
                        print(f"\nCantidad de países en {continente}: {cantidad}")
                    
                    elif op_estad == 0:
                        break

                except ValueError as e:
                    print(f"\n{e}")

        # ==========================
        # AGREGAR PAÍS
        # ==========================
        elif opcion == 5:
            try:
                print("\n===== AGREGAR PAÍS =====")
                paises = agregarPais(paises)
                print("\nPaís agregado correctamente.")
            except Exception as e:
                print(f"Se ha producido un error en el guardado: {e}")
                
        # ==========================
        # ACTUALIZAR POBLACIÓN
        # ==========================
        elif opcion == 6:
            try:
                print("\n===== ACTUALIZAR POBLACIÓN =====")
                paises = actualizarPobla(paises)
                print("\nPoblación actualizada correctamente.")
            except Exception as e:
                print(f"Se ha producido un error en el guardado: {e}")

        # ==========================
        # ACTUALIZAR SUPERFICIE
        # ==========================
        elif opcion == 7:
            try:
                print("\n===== ACTUALIZAR SUPERFICIE =====")
                paises = actualizarSuper(paises)
                print("\nSuperficie actualizada correctamente.")
            except Exception as e:
                print(f"Se ha producido un error en el guardado: {e}")    

        # ==========================
        # GUARDAR CAMBIOS
        # ==========================
        elif opcion == 8:
            try:
                guardarCambios(paises)
                print("Cambios guardados exitosamente.")
            except Exception as e:
                print(f"Se ha producido un error en el guardado: {e}")
                
        elif opcion == 0:
            print("\nSaliendo del programa.")
            break

if __name__ == "__main__":
    main()