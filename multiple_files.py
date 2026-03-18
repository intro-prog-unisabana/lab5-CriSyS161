from utils import *
#Pedir mensajes al usuario
mensaje = input("Please type your message\n")
#Invertir el mensaje
mensa_inv = flip(mensaje)
#Contar las letras a
cont_a = count_letters(mensa_inv, 'a')
#Imprimir resultado final
print(f"Your encoded message is: {mensa_inv}{cont_a}")