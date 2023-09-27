# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total de la compra
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada a la función con monto total y porcentaje de descuento predeterminado
monto_compra1 = 1200  # Monto total de la primera compra
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

# Llamada a la función con monto total y porcentaje de descuento personalizado
monto_compra2 = 2000  # Monto total de la segunda compra
porcentaje_descuento2 = 15  # Porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Mostrar los resultados
print("Resultado de la primera compra:")
print(f"Monto de compra: ${monto_compra1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")
print("\nResultado de la segunda compra:")
print(f"Monto de compra: ${monto_compra2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")