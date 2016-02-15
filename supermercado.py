product=["arroz", "leche", "tuna", "cereal", "jugo"]

print (product)
compras = []
def agregar():
    articulo = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    compras.append([articulo, cantidad])

def editar():
    producto = input("Producto a Editar: ")
    index = 0
    for e in compras:
        if producto == e[0]:
            cantidad = int(input("Cantidad: "))
            compras[index]=[e[0], cantidad]
            break
        index += 1

def eliminar():
    producto = input("Producto a Eliminar: ")
    index = 0
    for e in compras:
        if producto == e[0]:
            compras.remove(index)
            break
        index += 1

def mostrar():
    for e in compras:
        print("%20s x%5d" % (e[0], e[1]))

while True:
    print("Elija una Opción")
    print("1. Agregar Producto")
    print("2. Editar Producto")
    print("3. Eliminar Producto")
    print("4. Mostrar Productos")
    print("5. Salir")
    opcion = int(input("Opción: "))
    if opcion == 1:
        agregar()
    if opcion == 2:
        editar()
    if opcion == 3:
        eliminar()
    if opcion == 4:
        mostrar()
    if opcion == 5:
        break




