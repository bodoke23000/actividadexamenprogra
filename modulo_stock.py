def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion:\n"))
            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except:
            print("Debe seleccionar una opcion valida")


def validar_codigo(codigo, productos):
    if len(codigo.strip()) == 0:
        return False
    for llave in productos:
        if llave.upper() == codigo.upper():
            return False
    return True


def validar_nombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    else:
        return False


def validar_categoria(categoria):
    if len(categoria.strip()) > 0:
        return True
    else:
        return False


def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False


def validar_disponible(opcion):
    if opcion.strip().lower() == "s" or opcion.strip().lower() == "n":
        return True
    else:
        return False


def validar_stock(stock):
    if stock >= 0:
        return True
    else:
        return False


def validar_vendidos(vendidos):
    if vendidos >= 0:
        return True
    else:
        return False


def buscar_codigo(codigo, productos):
    for llave in productos:
        if llave.upper() == codigo.upper():
            return True
    return False


def obtener_llave_real(codigo, productos):
    for llave in productos:
        if llave.upper() == codigo.upper():
            return llave
    return None


def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    encontrado = False
    for codigo in productos:
        if productos[codigo][1].upper() == categoria.upper():
            encontrado = True
            total_stock = total_stock + inventario[codigo][0]
    if encontrado == True:
        print(f"\nEl stock total para la categoria '{categoria}' es: {total_stock}")
    else:
        print(f"\nNo existen productos registrados en la categoria '{categoria}'")


def buscar_precio(precio_min, precio_max, productos, inventario):
    resultados = []
    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]
        if precio >= precio_min and precio <= precio_max and stock > 0:
            resultados.append((productos[codigo][0], codigo))
    if len(resultados) == 0:
        print("\nNo se encontraron productos en ese rango de precio")
    else:
        resultados.sort()
        print(f"\nProductos entre ${precio_min} y ${precio_max}:")
        for producto in resultados:
            print(f"{producto[0]}--{producto[1]}")


def actualizar_precio(codigo, nuevo_precio, productos):
    llave_real = obtener_llave_real(codigo, productos)
    if llave_real != None:
        productos[llave_real][2] = nuevo_precio
        return True
    else:
        return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):
    if buscar_codigo(codigo, productos) == True:
        return False
    else:
        productos[codigo] = [nombre, categoria, precio, disponible]
        inventario[codigo] = [stock, vendidos]
        return True


def eliminar_producto(codigo, productos, inventario):
    llave_real = obtener_llave_real(codigo, productos)
    if llave_real != None:
        del productos[llave_real]
        del inventario[llave_real]
        return True
    else:
        return False


def mostrar_productos(productos, inventario):
    if len(productos) == 0:
        print("No hay productos para mostrar")
    else:
        for codigo in productos:
            print(f"""
CODIGO: {codigo}
--------------------------
Nombre: {productos[codigo][0]}
Categoria: {productos[codigo][1]}
Precio: ${productos[codigo][2]}
Disponible: {productos[codigo][3]}
Stock: {inventario[codigo][0]}
Vendidos: {inventario[codigo][1]}
--------------------------""")
