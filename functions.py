def promedio_estudiante(calificaciones):
    if not calificaciones: 
        return 0.0
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = float(suma / cantidad)
    return float(promedio)

calificaciones = [] 
promedio = promedio_estudiante(calificaciones)
print (promedio)