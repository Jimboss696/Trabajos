# Definir una matriz de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Valor que deseas buscar
valor_buscado = 5

# Realizar la búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición: fila {posicion[0] + 1}, columna {posicion[1] + 1}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
