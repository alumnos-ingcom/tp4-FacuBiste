

def convertir_fahrenheit(centigrados):
    return (centigrados * 9/5) + 32

numero = float(input("dime el numero para pasar a F: "))
print(convertir_fahrenheit(numero))





def convertir_a_centigrados(fahrenheit):
    return (fahrenheit - 32) * 5/9

numero2 = float(input("dime el numero para pasar a C: "))
print(convertir_a_centigrados(numero2))