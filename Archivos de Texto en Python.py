# Paso 1: Crear un nuevo archivo llamado my_notes.txt y escribir notas personales
with open("my_notes.txt", "w") as file:
    file.write("Notas personales:\n")
    file.write("1. Hoy es un día soleado.\n")
    file.write("2. Tengo que comprar víveres más tarde.\n")
    file.write("3. Recordar hacer ejercicio esta tarde.\n")

# Paso 2: Abrir el archivo my_notes.txt y leerlo línea por línea
with open("my_notes.txt", "r") as file:
    print("Contenido del archivo my_notes.txt:")
    for line in file.readlines():
        print(line.strip())  # Utilizamos strip() para eliminar caracteres de nueva línea

# Paso 3: Cerrar el archivo (esto se hace automáticamente con el uso de "with")