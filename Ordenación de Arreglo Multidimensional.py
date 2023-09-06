def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def ordenar_fila(matriz, fila):
    # Comprueba si la fila está dentro de los límites de la matriz
    if fila < 0 or fila >= len(matriz):
        print("Fila fuera de los límites de la matriz.")
        return

    # Ordena la fila utilizando el método sort
    matriz[fila].sort()

# Definir una matriz de ejemplo (3x3)
matriz = [
    [3, 1, 2],
    [6, 5, 4],
    [9, 8, 7]
]

# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Fila que deseas ordenar (0-indexed)
fila_a_ordenar = 1

# Ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
imprimir_matriz(matriz)