# Definimos las dimensiones de la matriz
ciudades = ["Quito", "Guayaquil", "Ambato"]  # Nombres de las ciudades
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]  # Días de la semana
semanas = 3  # Número de semanas

# Creamos la matriz 3D de temperaturas con valores aleatorios (en un rango de 10 a 35 grados)
import random

# Inicializamos la matriz de tamaño [ciudades][dias de la semana][semanas]
temperaturas = [[[random.uniform(10, 35) for _ in range(semanas)] for _ in range(len(dias_semana))] for _ in range(len(ciudades))]

# Mostrar la matriz de temperaturas
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas para {ciudad}:")
    for j, dia in enumerate(dias_semana):
        print(f"{dia}: {temperaturas[i][j]}")
    print("\n")

# Calcular el promedio de temperaturas para cada ciudad por semana
print("Promedio de temperaturas por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[i][dia][semana]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"Semana {semana + 1} en {ciudad}: {promedio:.2f} grados")
    print("\n")