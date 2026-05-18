
menu = [
    ["Hamburguesa", "Comida rápida", 18000],
    ["Pizza", "Comida rápida", 25000],
    ["Ensalada", "Saludable", 12000],
    ["Jugo Natural", "Bebida", 8000],
    ["Café", "Bebida", 5000],
    ["Postre", "Dulce", 10000]
]


print("------ MENÚ DEL RESTAURANTE ------")

for i in range(len(menu)):
    print(i + 1, "-", menu[i][0], "-", "$", menu[i][2])


opcion = int(input("\nSeleccione un producto del menú: "))


producto = menu[opcion - 1]

nombre = producto[0]
categoria = producto[1]
precio = producto[2]


def calcular_precio_final(categoria, precio):

    categoria_objetivo = "Comida rápida"
    umbral = 15000
 
    if categoria == categoria_objetivo and precio >= umbral:
        descuento = precio * 0.15
        precio_final = precio - descuento
        promocion = "15% de descuento"
    else:
        precio_final = precio
        promocion = "Sin promoción"

    return precio_final, promocion


precio_final, promo = calcular_precio_final(categoria, precio)


print("\n------ FACTURA ------")
print("Producto:", nombre)
print("Categoría:", categoria)
print("Precio Base: $", precio)
print("Precio Final: $", precio_final)
print("Promoción:", promo)