print("Me voy a la cocina")
print("Abro el refrigerador")

hay_leche = input("¿Hay leche? S/N ")
hay_chocolate = input("¿Hay chocolate? S/N ")

if hay_leche != "S" or hay_chocolate != "S":
    print("Ve al supermercado")
    if hay_leche != "S":
        print("Compra leche")
    if hay_chocolate != "S":
        print("Compra chocolate")

print("Echamos la leche al vaso")
print("Echamos el chocolate al vaso de leche")
print("Mezclamos el chocolate")
print("Esta listo, ahora puedes tomar :D")