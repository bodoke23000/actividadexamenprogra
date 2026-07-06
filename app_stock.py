import os
import modulo_stock as ms

productos = {}
inventario = {}

while True:
    os.system("cls")
    print("""
========== MENU PRINCIPAL ==========
1. Stock por categoria
2. Buscar productos por rango de precio
3. Actualizar precio
4. Agregar producto
5. Eliminar producto
6. Mostrar productos
7. Salir
===================================""")
    op = ms.leer_opcion()

    match (op):
        case 1:
            os.system("cls")
            categoria = str(input("Ingrese la categoria a consultar:\n")).strip()
            while not ms.validar_categoria(categoria):
                print("La categoria no puede estar vacia")
                categoria = str(input("Ingrese la categoria a consultar:\n")).strip()
            ms.stock_categoria(categoria, productos, inventario)
            os.system("pause")

        case 2:
            os.system("cls")
            while True:
                try:
                    precio_min = int(input("Ingrese el precio minimo:\n"))
                    if ms.validar_precio(precio_min):
                        break
                    else:
                        print("El precio debe ser un numero entero mayor a 0")
                except:
                    print("Error, ingrese solo numeros enteros")
            while True:
                try:
                    precio_max = int(input("Ingrese el precio maximo:\n"))
                    if ms.validar_precio(precio_max) and precio_max >= precio_min:
                        break
                    else:
                        print(
                            "El precio maximo debe ser mayor a 0 y mayor o igual al minimo"
                        )
                except:
                    print("Error, ingrese solo numeros enteros")
            ms.buscar_precio(precio_min, precio_max, productos, inventario)
            os.system("pause")

        case 3:
            continuar = "s"
            while continuar == "s":
                os.system("cls")
                codigo = str(
                    input("Ingrese el codigo del producto a actualizar:\n")
                ).strip()
                if ms.buscar_codigo(codigo, productos) == True:
                    while True:
                        try:
                            nuevo_precio = int(input("Ingrese el nuevo precio:\n"))
                            if ms.validar_precio(nuevo_precio):
                                break
                            else:
                                print("El precio debe ser un numero entero mayor a 0")
                        except:
                            print("Error, ingrese solo numeros enteros")
                    ms.actualizar_precio(codigo, nuevo_precio, productos)
                    print("El precio se actualizo correctamente")
                else:
                    print("Codigo inexistente")
                continuar = (
                    str(input("Desea actualizar otro precio? (s/n):\n")).strip().lower()
                )
            os.system("pause")

        case 4:
            os.system("cls")
            codigo = str(input("Ingrese el codigo del producto:\n")).strip()
            while not ms.validar_codigo(codigo, productos):
                print("El codigo no puede estar vacio o ya se encuentra registrado")
                codigo = str(input("Ingrese el codigo del producto:\n")).strip()

            nombre = str(input("Ingrese el nombre del producto:\n")).strip()
            while not ms.validar_nombre(nombre):
                print("El nombre no puede estar vacio")
                nombre = str(input("Ingrese el nombre del producto:\n")).strip()

            categoria = str(input("Ingrese la categoria del producto:\n")).strip()
            while not ms.validar_categoria(categoria):
                print("La categoria no puede estar vacia")
                categoria = str(input("Ingrese la categoria del producto:\n")).strip()

            while True:
                try:
                    precio = int(input("Ingrese el precio del producto:\n"))
                    if ms.validar_precio(precio):
                        break
                    else:
                        print("El precio debe ser un numero entero mayor a 0")
                except:
                    print("Error, ingrese solo numeros enteros")

            disponible_str = str(input("El producto esta disponible? (s/n):\n")).strip()
            while not ms.validar_disponible(disponible_str):
                print("Debe ingresar 's' o 'n'")
                disponible_str = str(
                    input("El producto esta disponible? (s/n):\n")
                ).strip()
            disponible = True if disponible_str.lower() == "s" else False

            while True:
                try:
                    stock = int(input("Ingrese el stock del producto:\n"))
                    if ms.validar_stock(stock):
                        break
                    else:
                        print("El stock debe ser mayor o igual a 0")
                except:
                    print("Error, ingrese solo numeros enteros")

            while True:
                try:
                    vendidos = int(input("Ingrese la cantidad vendida:\n"))
                    if ms.validar_vendidos(vendidos):
                        break
                    else:
                        print("Los vendidos deben ser mayor o igual a 0")
                except:
                    print("Error, ingrese solo numeros enteros")

            ms.agregar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                disponible,
                stock,
                vendidos,
                productos,
                inventario,
            )
            print("El producto se ha registrado correctamente")
            os.system("pause")

        case 5:
            os.system("cls")
            codigo = str(input("Ingrese el codigo del producto a eliminar:\n")).strip()
            if ms.eliminar_producto(codigo, productos, inventario) == True:
                print("El producto ha sido eliminado")
            else:
                print("Codigo inexistente")
            os.system("pause")

        case 6:
            os.system("cls")
            ms.mostrar_productos(productos, inventario)
            os.system("pause")

        case 7:
            os.system("cls")
            print("Gracias por usar el sistema. Vuelva pronto")
            break

        case _:
            os.system("cls")
            print("Debe seleccionar una opcion valida")
            os.system("pause")
