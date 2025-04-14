def validar(numero):
    return numero.isdigit() and  all (digito in '01'for digito in numero)
numero = input("ingresa un numero bianrio: ")
if validar(numero):
    print("el numero es binario")
else: print("el numero no es binario")





