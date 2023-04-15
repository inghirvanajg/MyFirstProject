import random

num_adivinar = random.randint(1,10)
print("Bienvenidos al juego de adivinanzas")

num_elegido = int(input("¿Tienes que adivinar el número escondido del 1-10?, escribe un número: "))

if num_elegido == num_adivinar:
    print("HAZ GANADO!! :D")
print("El número ganador es: {}".format(num_adivinar))
if num_elegido != num_adivinar:
    print("VUELVE A INTENTARLO :(")
if num_elegido > 10:
    print("El número es: {}, se ha pasado jajaja".format(num_elegido))