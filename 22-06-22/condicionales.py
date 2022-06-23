# Una pregunta -> Dos respues -> Es verdadero o Es Falso


num = 2

if num == 5:
    print("El numero es el mismo")
else:
    print("El numero es diferente")

print("Hola")

num = 12 
if num % 2 ==0 and num %3 ==0 and num%4 ==0:
    print("El numero es divisible por 2, 3 y 4")

if num % 5 == 0 or num % 6 == 0:
    # Only works when num is either a multiple of 5 or 6
    print("The number is a multiple of 5 and/or 6")


num = 24

if num == 2:
    print("Es igual a 2")
elif num > 26:
    print("El numero es grande")
elif num >8:
    print("El numro es mas grande que 8")
elif num %2 == 0:
    print("Es divisible por 2")
else:
    print("Este numero no tiene s")

texto = "Hola"
print(texto[1])


palabra = "palabra"
print(palabra[::-1])
