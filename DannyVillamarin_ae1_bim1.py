# Sistema de facturación de un cine

# Ingresamos las ventas a registrar en el cine durante el día
num_ventas = int(input("Ingrese el número de ventas a registrar en el día: "))

# Determinamos los arreglos para el ejercicio
nombres = []
apellidos = []
cantidades = []
precios = []
totales = []

i = 0

# Registro de las ventras del cine
while i < num_ventas:

    print("\n--- Registro de Ventas Diarias", i + 1, "---")

    nombre = input("Ingrese los nombres del cliente: ")
    apellido = input("Ingrese los apellidos del cliente: ")

    cantidad_entradas = int(input("Ingrese la cantidad de entradas adquiridas por el cliente: "))
    precio = float(input("Ingrese el precio unitario de cada entrada: "))

    # Cálculo del subtotal, determinado por la cantidad de entradas adquiridas y el precio de cada
    # sin aplicar el descuento todavía
    subtotal = cantidad_entradas * precio

    # Determinar el descuento que genera cada cliente
    if cantidad_entradas == 1:
        descuento_porcentaje = 0.10
    elif cantidad_entradas >= 2 and cantidad_entradas <= 3:
        descuento_porcentaje = 0.20
    elif cantidad_entradas >= 4 and cantidad_entradas <= 5:
        descuento_porcentaje = 0.30
    else:
        descuento_porcentaje = 0.40

    # Vamos calcular el descuento y el total a cancelar por el cliente
    descuento = subtotal * descuento_porcentaje
    total_pagar = subtotal - descuento

    # Guardar datos en cada arreglo
    nombres.append(nombre)
    apellidos.append(apellido)
    cantidades.append(cantidad_entradas)
    precios.append(precio)
    totales.append(total_pagar)

    # Mostrar resultados de la venta
    print("Resumen de la compra:")
    print("Cliente:", nombre, apellido)
    print("Subtotal: $", round(subtotal, 2))
    print("Descuento aplicado: $", round(descuento, 2))
    print("Total a pagar: $", round(total_pagar, 2))

    i += 1

#Mostramos el reporte final de las ventas

print("REPORTE FINAL DE VENTAS")

i = 0
suma_totales = 0

while i < num_ventas:

    print("Venta", i + 1)
    print("Nombre:", nombres[i])
    print("Apellido:", apellidos[i])
    print("Cantidad de entradas:", cantidades[i])
    print("Precio unitario: $", precios[i])
    print("Total pagado: $", round(totales[i], 2))

    suma_totales += totales[i]

    i += 1

# Promedio de ventas
promedio = suma_totales / num_ventas

# Venta mayor y menor
venta_mayor = max(totales)
venta_menor = min(totales)

indice_mayor = totales.index(venta_mayor)
indice_menor = totales.index(venta_menor)

# Mostramos el promedio de ventas

print("ESTADISTICAS MULTICINES")
print("Promedio de ventas: $", round(promedio, 2))

print("Venta de mayor monto:")
print(nombres[indice_mayor], apellidos[indice_mayor],
      "- $", round(venta_mayor, 2))

print("Venta de menor monto:")
print(nombres[indice_menor], apellidos[indice_menor],
      "- $", round(venta_menor, 2))