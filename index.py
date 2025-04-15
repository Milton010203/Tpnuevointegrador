# Realizamos las funciones de conversion
def decimal_a_binario(numero):
    if numero == 0:
        return "0"

    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2
    return binario

def binario_a_decimal(numero):
    decimal = 0
    potencia = 0
    for digito in reversed(numero):
        if digito == '1':
            decimal += 2 ** potencia
        elif digito != '0':
            return "Entrada no válida: solo se permiten 0s y 1s"
        potencia += 1

    return decimal

# Realizamos la fucion para que solo ingresen numero binarios por consola
def validar(numero):
    return numero.isdigit() and  all (digito in '01'for digito in numero)

# Se genera una bandera para diferenciar cuando se ingresa un valor valido o invalido en el menu de opciones
flag = False

while flag == False:
    # Se crea el menu de opciones
    print("- " * 50)
    opcion = int(input("1. Conversion de decimal a binario\n" \
    "2. Conversion de binario a decimal\n" \
    "Ingrese su opcion: "))
    print("- " * 50)
    flagger = False


    if opcion == 1:
        # Se genera un ciclo para repetir el bloque en caso de ingresar un valor invalido
        while flagger == False:
            # Se intenta ejecutar el codigo...
            try:
                # Se le pide un valor al usuario
                num = int(input("Ingrese un numero decimal: "))

                # Si el valor es menor a 0 devuelve un error
                if num < 0:
                    print("Ingrese un numero positivo")
                    print("- " * 50)

                # Si el valor es correcto, hace la conversion
                else:
                    binario = decimal_a_binario(num)
                    print(f"El número {num} en binario es {binario}")
                    flagger = True
            # Si el valor no es un numero, tambien devuelve un error
            except ValueError:
                print("Inrgese un valor valido")
                print("- " * 50)
        flag = True

    # Segunda opcion
    elif opcion == 2:
        # Se genera un ciclo para repetir el bloque en caso de ingresar un valor invalido
        while flagger == False:
            # Se intenta ejecutar el codigo...
            try:
                # Se le pide un valor binario al usuario
                num = input("Ingrese un numero binario: ")

                # Validacion de ingreso de numeros binarios
                if validar(num):
                    # Si el numero es binario se realiza la conversion
                    numdecimal = binario_a_decimal(num)
                    print(f"El número {num} en decimal es {numdecimal}")
                    flagger = True
                else:
                    # Si el valor ingresado no es binario se informa por consola y se pide ingresar otro valor
                    print("El numero ingresado no es un binario")
                    print("- " * 50)
            # Se inserta un except para poder ejecutar correctamente el try        
            except ValueError:
                print("Inrgese un valor valido")
                print("- " * 50)
        # Una vez terminado el ciclo de ingreso de numeros y se haya hecho la conversion
        # Se sube la bandera para que no se ejecute de vuelta el menu de opciones       
        flag = True

    # En caso de no ingresar ninguna de las opciones propuestas, se informa por consola y se pide que ingrese otro valor    
    else:
        print("Ingresa una opcion valida")

