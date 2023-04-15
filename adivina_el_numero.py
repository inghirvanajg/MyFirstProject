print("Bienvenidos al juego de adivinanzas")
num_adivinar = 7

numero = int(input("¿Tienes que adivinar el número del 1-10?, escribe un número: "))
if numero <= 10:
    print("El número que haz ingresado es: {}, corresponde del 1-10".format(numero))
    if numero != num_adivinar:
        print("INTENTALO DE NUEVO :(")
    if numero == num_adivinar:
        print("HAZ GANADO :D !!!")
