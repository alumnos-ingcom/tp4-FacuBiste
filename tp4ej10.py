

def factores_primos(numero):   
    print(numero,"--> ", end="") 
    factor_primo = 2

    primer_factor = True
    while numero > 1:
        if numero % factor_primo == 0:
            if primer_factor:
                primer_factor = False
            else:
                print(end=",")
            print(factor_primo, end="")
            numero /= factor_primo            
        else:  
            factor_primo += 1        
    
numero = int(input("Ingrese un número mayor a 1: "))

factores_primos(numero)