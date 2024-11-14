productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5},
                     {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}],
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5},
                     {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}],
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0},
                     {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8},
                     {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

def agregar_producto(almacen, nombre, cantidad, precio, estanteria):
    estanteria_productos = almacen[estanteria]
    for producto in estanteria_productos:
        if producto["nombre"] == nombre: #Compara los productos que ya hay para saber si ya existe
            producto["cantidad"] += cantidad #Si existe, le añade la cantidad
            print(f"Se ha añadido {cantidad} unidades de {nombre} a la estantería.")
            if producto["precio"] != precio: #Y si el precio es distinto, lo actualiza
                producto["precio"] = precio
                print(f"Se ha actualizado el precio de {nombre} a {precio}.")
            return
        else:
            producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
            almacen[estanteria].append(producto) #Si el producto no estaba en la estantería, lo añade como producto nuevo
            print(f"El producto {nombre} se ha agregado correctamente.")
            return

def retirar_producto(almacen, nombre, cantidad):
    for estanteria, productos in almacen.items():
        for producto in productos: #Recorre todos los productos de todas las estanterias para saber si está y donde está
            if producto["nombre"] == nombre: 
                if producto["cantidad"] < cantidad: 
                    print(f"No se hay cantidad suficiente de {nombre}.") #Si pones mayor cantidad de la que hay, no hace nada
                    return
                elif producto["cantidad"] == cantidad: #Si pones la misma, elimina el producto
                    productos.remove(producto)
                    print(f"Se ha agotado el producto {nombre}")
                    return
                else:
                    producto["cantidad"] -= cantidad #Si pones menos, lo resta
                    print(f"Se ha retirado {cantidad} unidades de {nombre} correctamente.")
                    return
            else:
                print(f"El producto {nombre} no existe en el almacen.")
            
def disponibilidad_producto(almacen, nombre):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre: #Recorre todos los productos, y si está en alguna estanteria te lo dice
                print(f"El producto {nombre} está disponible en la {estanteria} con {producto["cantidad"]} unidades.")
            else:
                print(f"El producto {nombre} no está disponible")
                return

def listar_productos(almacen):
    for estanteria, productos in almacen.items():
        print(f"{estanteria}:")
        if productos: #Recorre todos los productos de todas las estanterias y te dice por cada estanteria, que producto, cuanto hay, que precio
            for producto in productos:
                print(f"   - {producto['nombre']} ({producto['cantidad']} unidades) a {producto['precio']}.")
        else:
            print("   No hay productos en esta estantería.")
        print()

def transferencia_producto(almacen, nombre, cantidad, estanteria1, estanteria2):
    estanteria1_productos = almacen[estanteria1]
    producto_origen = None
    for producto in estanteria1_productos: #Aquí busca si el producto está en la estanteria origen
        if producto["nombre"] == nombre:
            producto_origen = producto
            break
    if producto_origen is None: #Si no está, no hace nada y termina el codigo
        print(f"El producto {nombre} no se encuentra en la {estanteria1}.")
        return
    cantidad_transferir = min(cantidad, producto_origen["cantidad"]) #Compara la cantidad especificada con la que hay de producto, y coge la menor
    agregar_producto(almacen, nombre, cantidad_transferir, producto_origen["precio"], estanteria2) #Actualiza la estantería destino con el metodo agregar_producto() de antes
    producto_origen["cantidad"] -= cantidad_transferir #Resta la cantidad transferida a la estanteria origen
    if producto_origen["cantidad"] == 0: #Si la cantidad es 0, elimina el producto
        estanteria1_productos.remove(producto_origen)
    print(f"Se ha transferido {cantidad_transferir} unidades de {nombre} correctamente.")


"""
listar_productos(productos_almacen)
agregar_producto(productos_almacen, "Chocolate Amargo", 10, 2.5, "Estantería A")
listar_productos(productos_almacen)
retirar_producto(productos_almacen, "Pasta Integral", 30)
listar_productos(productos_almacen)
disponibilidad_producto(productos_almacen, "Pasta Integral")
transferencia_producto(productos_almacen, "Café Molido", 25, "Estantería C", "Estantería B")
listar_productos(productos_almacen)
"""