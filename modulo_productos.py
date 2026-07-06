productos_list=[]

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

def validar_codigo(codigo, productos):
    if len(codigo.strip()) > 0:
        for llave in productos:
            if llave.upper() == codigo.upper():
                return False
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