

def es_primo(numero):
    if numero % 2 != 0:
        print(False)
    else:
        print(True)

numero = int(input("dame un numero: "))
es_primo(numero)