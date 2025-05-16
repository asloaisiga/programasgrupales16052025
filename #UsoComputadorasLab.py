#USO DE COMPUTADORAS EN 2 DE LOS LABORATORIOS DEL CAMPUS
#EJERCICIO 1
"""Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del
campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora
se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con
valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras
ocupadas y libres por laboratorio."""

#Se declaran valores para las variables:
laboratorios=2 #Cantidad de laboratorios
filas=5 #Cantidad de filas por laboratorio
computadoras=4 #Cantidad de computadoras por fila

#Se declaran los contadores por laboratorio:
ocupadas1=0 #Contador de computadoras ocupadas en el laboratorio 1
ocupadas2=0 #Contador de computadoras ocupadas en el laboratorio 2
libres1=0 #Contador de computadoras libres en el laboratorio 1
libres2=0 #Contador de computadoras libres en el laboratorio 2

#Bucle para recorrer los laboratorios:
for laboratorios in range(1,3):
    #Se declaran los contadores por fila:
    ocupadas=0 #Contador de computadoras ocupadas en el laboratorio i
    libres=0 #Contador de computadoras libres en el laboratorio i
    print ("Laboratorio ", laboratorios, " :")
    
    #Bucle para recorrer las filas:
    for filas in range(1,6):
        #Bucle para recorrer las computadoras:
        for computadoras in range(1,5):
            #Se pide al usuario que ingrese el estado de la computadora:
            estado=input("La computadora numero " + str(computadoras) + " de la fila  " + str(filas) + " está ocupada o libre? (O/L): ")
            #Se verifica si el usuario ingresó un valor válido:
            while estado != "O" and estado != "L":
                print("Estado inválido. Ingrese O o L.")
                estado=input("La computadora numero " + str(computadoras) + " de la fila  " + str(filas) + " está ocupada o libre? (O/L): ")
            #Se hace un conteo de las computadoras ocupadas y libres:
            if estado == "O":
                ocupadas += 1
            else:
                libres += 1
        #Se muestran los resultados por laboratorio:
    if laboratorios == 1 :
        ocupadas1 = ocupadas
        libres1 = libres
    else:
        ocupadas2 = ocupadas
        libres2 = libres
        
#Se muestran los resultados finales:
print("Laboratorio 1 - Ocupadas: ", ocupadas1, ", Libres: ", libres1) 
print("Laboratorio 2 - Ocupadas: ", ocupadas2, ", Libres: ", libres2)
print("Fin del programa")

    
    