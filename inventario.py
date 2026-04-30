def contar_productos():
    inventario = {}
    
    while True:
        producto = input("Ingrese el producto (o FIN para terminar): ").upper()
        
        if producto == "FIN":
            break
        
        registrar_venta(producto, inventario)
    
    return inventario


def registrar_venta(producto, inventario):
    if producto in inventario:
        inventario[producto] += 1
    else:
        inventario[producto] = 1


def mostrar_resumen(inventario):
    print("\nResumen de ventas:")
    
    for producto, cantidad in inventario.items():
        print(f"{producto.capitalize()}: {cantidad}")
    
    mas_vendido = max(inventario, key=inventario.get)
    print(f"\nProducto más vendido: {mas_vendido.capitalize()} ({inventario[mas_vendido]})")



def agregar_inventario(inventario):
    while True:
        producto = input("Ingrese producto (o FIN para terminar): ").upper()
        
        if producto == "FIN":
            break
        
        cantidad = int(input("Ingrese cantidad: "))
        
        if producto in inventario:
            inventario[producto] += cantidad
        else:
            inventario[producto] = cantidad



def vender_productos(inventario, ventas):
    while True:
        producto = input("Ingrese producto a vender (o FIN para terminar): ").upper()
        
        if producto == "FIN":
            break
        
        if producto in inventario and inventario[producto] > 0:
            inventario[producto] -= 1
            registrar_venta(producto, ventas)
            print("Venta realizada")
        else:
            print("No hay stock disponible")



inventario = {}
ventas = {}

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar productos al inventario")
    print("2. Vender productos")
    print("3. Mostrar resumen de ventas")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_inventario(inventario)
    
    elif opcion == "2":
        vender_productos(inventario, ventas)
    
    elif opcion == "3":
        if ventas:
            mostrar_resumen(ventas)
        else:
            print("No hay ventas registradas")
    
    elif opcion == "4":
        print("Programa finalizado")
        break
    
    else:
        print("Opción inválida")