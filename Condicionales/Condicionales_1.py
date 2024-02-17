print("Programa de evaluacion de notas de ALUMNOS")

notaAlumno=input("introduce la calificacion: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<=5:
        valoracion="reprobado"
    return valoracion

print(evaluacion(int(notaAlumno)))