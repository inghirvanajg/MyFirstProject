numero_1 = int(input("Escribe el primer número: "))
numero_2 = int(input("Escribe el segundo número: "))
numero_3 = int(input("Escribe el tercer número: "))

print("Entre los 3 números {}, {} y {}, el mayor es {} y el menor es {}".format(numero_1, numero_2, numero_3,
                                                                         max(numero_1, numero_2, numero_3),
                                                                         min(numero_1, numero_2, numero_3)))