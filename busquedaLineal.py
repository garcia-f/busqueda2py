import timeit 
print("-------------------------------------------")
print("Busqueda Lineal")
print("-------------------------------------------")
def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  # Devuelve el índice si se encuentra el objetivo
    return -1  # Devuelve -1 si el objetivo no está en la lista

# Ejemplo de uso
mi_lista = [10, 20, 30, 40, 50]
objetivo = 30
print("Tiempo de ejecución:", timeit.timeit(lambda: busqueda_lineal(mi_lista, objetivo), number=1))
resultado = busqueda_lineal(mi_lista, objetivo)
if resultado != -1:
    print(f"El objetivo {objetivo} se encuentra en la posición {resultado}.")
else:
    print(f"El objetivo {objetivo} no está en la lista.")
print("-------------------------------------------")