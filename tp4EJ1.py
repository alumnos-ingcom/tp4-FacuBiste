################
# Facundo Bistevins - @facundobistevins@gmail.com
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################



# 1)

def ingreso_entero(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No es el numero ") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    while cantidad_reintentos >0:
        try:
            valor = ingreso_entero(mensaje)
            return valor
        except IngresoIncorrecto as error:
            cantidad_reintentos = cantidad_reintentos - 1
            print(f"te quedan {cantidad_reintentos}")
    raise IngresoIncorrecto("No mas intentos")

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    pass

class IngresoIncorrecto(Exception):
    pass

def prueba():
    print("hola ")
    minumero = ingreso_entero("ingrese un numero: ")
    print(f"mi numero es {minumero}")

if __name__ == "__main__":
    prueba()
