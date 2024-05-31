import timeit
print("-------------------------------------------")
print("Busqueda Binaria")
print("-------------------------------------------")
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de uso (la lista debe estar ordenada)
mi_lista_ordenada = [10, 20, 30, 40, 50]
objetivo = 30
print("Tiempo de ejecución:", timeit.timeit(lambda: busqueda_binaria(mi_lista_ordenada, objetivo), number=1))
resultado = busqueda_binaria(mi_lista_ordenada, objetivo)
if resultado != -1:
    print(f"El objetivo {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El objetivo {objetivo} no está en la lista.")
print("-------------------------------------------")