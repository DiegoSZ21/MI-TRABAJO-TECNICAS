# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 10:10:36 2025

@author: diego
"""

#definir notas de estudiantes

estudiantes=[]

n=int(input("Ingrese la cantidad de estudiantes: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
    estudiantes.append((nombre, calificacion))

suma_calificaciones = 0

for _, calificacion in estudiantes:
    suma_calificaciones += calificacion

promedio = suma_calificaciones / n

aprobados = []

for nombre, calificacion in estudiantes:
    if calificacion >= 12:
        aprobados.append(nombre)

print("Los estudiantes aprobados son:")
for estudiante in aprobados:
    print(f"- {estudiante}")

print(f"\nEl promedio general del grupo es: {promedio:.2f}")