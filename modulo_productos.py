productos_list=[]

def validar_texto_vacio(texto):
    if len(texto.strip())>0:
        return True
    else:
        print("Error, el texto no puede ser vacio")

def numero_positivo(numero):
    if numero>0:
        return True
    else:
        print("Error, el numero debe ser mayor a 0")

def esta_disponible(producto):
    if esta_disponible=="si":
        producto["disponible"]=True
    elif esta_disponible=="no":
        producto["disponible"]=False
