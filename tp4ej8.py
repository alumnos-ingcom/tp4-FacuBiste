


def ordenar_mayor_a_menor(numero1, numero2, numero3):
    
    numeros = [numero1, numero2, numero3]
    numeros.sort(reverse=True)
    print (numeros)
    
numero1 = int(input("dame un numero: "))
numero2 = int(input("dame un numero: "))
numero3 = int(input("dame un numero: "))

ordenar_mayor_a_menor(numero1, numero2, numero3)


print("\n")
print("*********************************")



def ordenar_menor_a_mayor(uno, dos, tres):
    numeros = [uno, dos, tres]
    numeros.sort()
    print (numeros)
    
uno = int(input("dame un numero: "))
dos = int(input("dame un numero: "))
tres = int(input("dame un numero: "))

ordenar_menor_a_mayor(uno, dos, tres)