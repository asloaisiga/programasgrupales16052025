#Crear un algoritmo para guardar consumo de cada edificio
#EJERCICIO 3
"""Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
generar el promedio semanal correspondiente."""
consumos_edificios = []  

#Recorrer los 4 edificios 
for edificio in range(1, 5):
    print(f"Edificio {edificio}")
    consumo_total = 0
    consumos_dias = []  #Guardar consumos diarios

    #Recorrer los 7 días de la semana
    for dia in range(1, 8):
        print(f"Día {dia}:")
        consumos_turnos = []  # Guardar consumos por turno del día

        #Recorrer los 3 horarios: mañana, tarde, noche
        for horario in range(1, 4):
            if horario == 1:
                print("  Escriba el consumo de kilovatios del turno de la Mañana:")
            elif horario == 2:
                print("  Escriba el consumo de kilovatios del turno de la Tarde:")
            elif horario == 3:
                print("  Escriba el consumo de kilovatios del turno de la Noche:")

            # Leer el consumo ingresado
            consumo = float(input("    Ingrese el consumo : "))

            consumo_total += consumo
            consumos_turnos.append(consumo)

        consumos_dias.append(consumos_turnos)

    promedio_semanal = consumo_total / 21  # 7 días * 3 horarios
    print(f"Consumo total del edificio {edificio}: {consumo_total:.2f} kWh")
    print(f"Promedio semanal del edificio {edificio}: {promedio_semanal:.2f} kWh\n")

    # Guardar los datos del edificio
    consumos_edificios.append({
        "edificio": edificio,
        "total": consumo_total,
        "promedio": promedio_semanal,
        "consumos": consumos_dias  # Lista de 7 días de la semana, cada uno con 3 consumos
    })
print("\nResumen de consumos por edificio:")
for datos in consumos_edificios:
    print(f"Edificio {datos['edificio']}: Total = {datos['total']:.2f} kWh, Promedio = {datos['promedio']:.2f} kWh")
