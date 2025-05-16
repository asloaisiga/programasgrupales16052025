# calcular el total de una feria estudiantil en UAM
"""Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
producto y mostrar un resumen por stand, por día, y un total general de la feria."""
# Datos iniciales
dias = 3
stands_por_dia = 4
productos_por_stand = 3

total_general = 0  # Contador total de ventas en toda la feria

# Bucle por cada día
for dia in range(1, dias + 1):
    print(f"\nDía {dia}")
    total_dia = 0  # Contador de ventas del día

    # Bucle por cada stand en el día
    for stand in range(1, stands_por_dia + 1):
        print(f"\nStand {stand}")
        total_stand = 0  # Contador de ventas por stand

        # Bucle por cada producto del stand
        for producto in range(1, productos_por_stand + 1):
            while True:
                try:
                    venta = float(input(f"Ingrese venta del Producto {producto}: $"))
                    break
                except ValueError:
                    print("Entrada inválida. Intente con un número válido.")

            total_stand += venta
            total_dia += venta
            total_general += venta

        # Mostrar resumen por stand
        print(f"Total de ventas del Stand {stand}: ${total_stand:.2f}")

    # Mostrar resumen por día
    print(f"\nTotal de ventas del Día {dia}: ${total_dia:.2f}")

# Mostrar total general
print(f"\nTOTAL GENERAL DE VENTAS EN LA FERIA: ${total_general:.2f}")
