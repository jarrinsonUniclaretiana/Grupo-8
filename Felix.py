#
# LIQUIDACIÓN JARCO SAS
#

# Entrada de datos
nombre = input("Nombre del vendedor: ")

salario_base = float(input("Salario base: "))
ventas = float(input("Ventas del mes: "))
horas_extras = int(input("Horas extras trabajadas: "))

# Proyectos
wordpress = int(input("Cantidad de proyectos WordPress: "))
woocommerce = int(input("Cantidad de proyectos WooCommerce: "))
custom = int(input("Cantidad de proyectos Custom: "))

#
# COMISIÓN
#

comision = ventas * 0.07

#
# HORAS EXTRAS
#

pago_horas_extras = 0

# Limitar máximo a 60 horas
if horas_extras > 60:
    horas_extras = 60

# Horas entre 41 y 50
if horas_extras >= 41:
    horas_18k = min(horas_extras, 50) - 40
    pago_horas_extras += horas_18k * 18000

# Horas mayores a 50
if horas_extras > 50:
    horas_25k = horas_extras - 50
    pago_horas_extras += horas_25k * 25000

# PUNTOS DE PROYECTOS
#

puntos = (
    (wordpress * 1) +
    (woocommerce * 2) +
    (custom * 3)
)

#
# BONO
#

bono = 0

if ventas > 3000000 and puntos >= 5:
    bono = 250000

#
# TOTAL LIQUIDACIÓN
#

total = salario_base + comision + pago_horas_extras + bono

#
# VENDEDOR ESTRELLA
#

vendedor_estrella = False

if total > 4200000:
    vendedor_estrella = True

#
# RESULTADOS
#

print("\n========== LIQUIDACIÓN ==========")
print(f"Vendedor: {nombre}")
print(f"Salario base: ${salario_base:,.0f}")
print(f"Comisión: ${comision:,.0f}")
print(f"Horas extras: ${pago_horas_extras:,.0f}")
print(f"Bono: ${bono:,.0f}")
print(f"Puntos obtenidos: {puntos}")
print(f"TOTAL A PAGAR: ${total:,.0f}")

if vendedor_estrella:
    print("\n⭐ Clasifica como VENDEDOR ESTRELLA")
    print("🎉 Obtiene un día libre adicional")
else:
    print("\nNo clasifica como Vendedor Estrella")