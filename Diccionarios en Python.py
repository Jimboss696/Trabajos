# Paso 1: Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Juan Perez",
    "edad": 30,
    "ciudad": "Ciudad A",
    "profesion": "Ingeniero"
}

# Paso 2: Acceder y modificar valores
# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Ciudad B"
# Agregar una nueva clave-valor que representa la "profesion"
informacion_personal["profesion"] = "Programador"

# Paso 3: Verificar existencia de claves
# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "555-1234"

# Paso 4: Eliminar una clave
# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Paso 5: Imprimir el diccionario final
print(informacion_personal)