def pedir_nota(materia):
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {materia} (0 - 5): "))
            if 0 <= nota <= 5:
                return nota
            else:
                print("Nota inválida, debe estar entre 0 y 5.")
        except ValueError:
            print("Ingrese un número válido.")


mat = pedir_nota("Matemáticas Discretas")
prog = pedir_nota("Programación II")
bd = pedir_nota("Bases de Datos")
proy = pedir_nota("Proyecto Integrador")


while True:
    try:
        faltas = int(input("Ingrese número de inasistencias: "))
        if faltas >= 0:
            break
        else:
            print("Ingrese un número válido (0 o mayor)")
    except ValueError:
        print("Ingrese un número entero válido.")


promedio = (mat * 0.30) + (prog * 0.25) + (bd * 0.25) + (proy * 0.20)

if 1 <= faltas <= 3:
    promedio -= 0.2
elif 4 <= faltas <= 6:
    promedio -= 0.5

promedio = max(0, promedio)


if faltas >= 7:
    estado = "Pierde por inasistencias"
else:
    if promedio >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"


if prog < 3.0:
    materia_riesgo = "Debe repetir Programación II"
else:
    materia_riesgo = "Ninguna"


if promedio >= 4.8:
    beca = "Honores - Beca del 20%"
else:
    beca = "Sin beca"


print("\\n--- RESULTADOS ---")
print(f"Promedio final: {round(promedio,2)}")
print(f"Estado: {estado}")
print(f"Beca: {beca}")
print(f"Materias en riesgo: {materia_riesgo}")