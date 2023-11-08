
#Programa de reconocer el caracter 

caracter = (input("Ingrese un caracter: "))

if 48 <= ord(caracter) <= 57:
print("El caracter es un numero")
elif "a" <= caracter <= "z" or  ord(caracter) == 241:
    print("El caracter es una letra minuscula")
else:
    print ("El caracter es una letra mayuscula")
