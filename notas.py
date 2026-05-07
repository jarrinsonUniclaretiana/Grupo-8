def pedir_nota(materia):
    while True:
        nota = float(input(f"Ingrese la nota de {materia} (0 - 5): "))
        if 0 <= nota <= 5:
            return nota
        else:
            print("Nota inválida, debe estar entre 0 y 5.")


mat = pedir_nota("Matemáticas Discretas")
prog = pedir_nota("Programación II")
bd = pedir_nota("Bases de Datos")
proy = pedir_nota("Proyecto Integrador")


faltas = int(input("Ingrese número de inasistencias: "))

# Promedio ponderado
promedio = (mat * 0.30) + (prog * 0.25) + (bd * 0.25) + (proy * 0.20)

# Penalización por inasistencias
if 1 <= faltas <= 3:
    promedio -= 0.2
elif 4 <= faltas <= 6:
    promedio -= 0.5
elif faltas >= 7:
    estado = "Pierde por inasistencias"
else:
    estado = "Sin estado"

# Estado académico
if faltas < 7:
    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

if prog < 3.0:
    materia_riesgo = " Debe repetir Programación II"
else:
    materia_riesgo = "Ninguna"


if promedio >= 4.8:
    beca = " Honores - Beca del 20%"
else:
    beca = "Sin beca"


print("\n--- RESULTADOS ---")
print(f"Promedio final: {round(promedio,2)}")
print(f"Estado: {estado}")
print(f"Beca: {beca}")
print(f"Materias en riesgo: {materia_riesgo}")