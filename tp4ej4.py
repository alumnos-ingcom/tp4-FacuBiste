


def compara(numero1, numero2):
    if numero1 < numero2:
        print("-1")
    elif numero1 == numero2:
        print("0")
    elif numero1 > numero2:
        print("1")

numero1 = int(input("dame el numero1: "))
numero2 = int(input("dame el numero2: "))

compara(numero1, numero2)