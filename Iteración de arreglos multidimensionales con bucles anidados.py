# Matriz 3D [ciudad][semana][día de la semana]
temperaturas = [
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
    ],
    [
        [33, 34, 35, 34, 32, 31, 30],
        [31, 30, 29, 28, 27, 28, 29],
        [28, 29, 30, 31, 30, 29, 28],
        [34, 35, 36, 35, 34, 33, 32]
    ]
]


# Función para calcular el promedio de temperaturas por ciudad
def calcular_promedio_ciudad(temperaturas):
    promedios_ciudades = []

    try:
        ciudades = len(temperaturas)
        semanas = len(temperaturas[0])
        dias_semana = len(temperaturas[0][0])

        for ciudad in range(ciudades):
            total_temperaturas_ciudad = 0
            total_dias = 0

            for semana in range(semanas):
                for dia in range(dias_semana):
                    total_temperaturas_ciudad += temperaturas[ciudad][semana][dia]
                    total_dias += 1

            promedio_ciudad = total_temperaturas_ciudad / total_dias
            promedios_ciudades.append(promedio_ciudad)

    except IndexError:
        print("Error: La estructura de datos de temperaturas no es válida.")
        return []

    return promedios_ciudades


# Ejemplo de uso de la función con tus datos
promedios = calcular_promedio_ciudad(temperaturas)

if promedios:
    for i, promedio in enumerate(promedios):
        print(f"Promedio de temperaturas para Ciudad {i + 1}: {promedio:.2f}°C")
else:
    print("No se pudieron calcular los promedios debido a un error en la estructura de datos.")