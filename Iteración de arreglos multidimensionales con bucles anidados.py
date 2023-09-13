# Paso 1: Crear una matriz 3D con datos de temperaturas
# Supongamos que tenemos tres ciudades, siete días de la semana y cuatro semanas.
# Puedes inicializar la matriz con datos de temperaturas ficticias.

# Matriz 3D [ciudad][día de la semana][semana]
temperaturas = [
    [
        [
            [28, 29, 30, 31, 28, 27, 29],
            [29, 30, 30, 32, 31, 30, 29],
            [27, 28, 28, 29, 30, 29, 28],
            [30, 31, 32, 32, 31, 30, 30]
        ],
        [
            [31, 32, 33, 32, 31, 30, 30],
            [29, 28, 30, 31, 29, 30, 29],
            [30, 31, 32, 31, 30, 29, 28],
            [32, 33, 34, 33, 32, 31, 30]
        ]
    ],
    [
        [
            [33, 34, 35, 34, 32, 31, 30],
            [31, 30, 29, 28, 27, 28, 29],
            [28, 29, 30, 31, 30, 29, 28],
            [34, 35, 36, 35, 34, 33, 32]
        ],
        [
            [36, 37, 36, 35, 34, 33, 32],
            [32, 31, 30, 29, 28, 27, 28],
            [30, 29, 31, 32, 32, 31, 30],
            [37, 38, 39, 38, 37, 36, 35]
        ]
    ],
    [
        [
            [29, 30, 30, 31, 29, 28, 29],
            [28, 27, 26, 27, 28, 29, 30],
            [30, 31, 32, 31, 30, 29, 28],
            [31, 32, 33, 34, 33, 32, 31]
        ],
        [
            [30, 31, 32, 31, 30, 29, 28],
            [29, 28, 27, 28, 29, 30, 31],
            [32, 33, 34, 35, 34, 33, 32],
            [33, 34, 35, 36, 35, 34, 33]
        ]
    ]
]

# Paso 2: Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = len(temperaturas)
semanas = len(temperaturas[0][0])

for ciudad in range(ciudades):
    for semana in range(semanas):
        total_temperaturas = 0
        dias = len(temperaturas[ciudad][0][semana])
        for dia in range(dias):
            total_temperaturas += sum(temperaturas[ciudad][d][semana][dia] for d in range(2))
        promedio = total_temperaturas / (dias * 2)  # Promedio para 2 semanas
        print(f"Promedio de temperaturas para Ciudad {ciudad + 1}, Semana {semana + 1}: {promedio:.2f}°C")

