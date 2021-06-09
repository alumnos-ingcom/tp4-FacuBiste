


def signo(numero):
    if numero > 0:
        print(f"El numero {numero}, es positivo")
    elif numero < 0:
        print(f"El numero {numero}, es negativo")
    elif numero == 0:
        print("el numero es 0")
    
numero = int(input("introduce un numero: "))

signo(numero)