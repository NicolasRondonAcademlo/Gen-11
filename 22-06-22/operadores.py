# 5 main
# Aritmeticos
# Comparacion
# Asignacion
# Logicos
# BitWise 

## Aritmeticos
# ()
# **
# %,*,/,//
# + -

adicion = 14+87
print(adicion)

float1= 14.8
float2 = 89.78

float_result = float1 + float2
print(float_result)

print(10-5)

num = 20
flt = 10.5

# float, int, str, list, tuple
result = int(num - flt)
print(type(str(88)))
print(result)

num = 45*2.5
print(num)

num = 40/10
print(num)
num = 40 // 10
print(num)

num = 2**4 # 2 * 2 *2*2
print(num)

num = 10 % 2
print(num)


print(10-3*2) # Multiplica - Resta 

print(3*20 /5)

print(3 / 20 * 5)


print((10-3) * 2)

# comparasion - > Siempre retornan un booleano (True, False)

a = 8> 2 # Mayor que
b = 5< 3 # Menor que
print(a,b)

c = 5>= 5
d = 5> 5
print(c)
print(d)


e = 6 <= 8
print(e)


f = 8  == 8 # === El triple no existe en python
print(f)

h = 2 != 3
print(h)

num2 = 10
num3 = 10


list1 = [6,7,8]
list2 = [6,7,8]

print(list1 is list2)
print(num2 is not num3)


# ASignacion

name = "Nicolas"
year = 2022 
year += 1
print(year)
year -= 1
print(year)

year *= 2
print(year)

year /= 2
print(year)

year //=4
print(year)

num = 2 
num **=3
print(num)


# logicos
# and or not

my_bool = True or False
print(my_bool)

my_bool = True and False
print(my_bool)

my_bool = False
print(not my_bool)

# True 1 False 0

print(15*True) 

house = "Gryffindor"
house_copy = "Gryffindor3"
print(house < house_copy)


# 
x = 20
y = 5
result = (x + True) / (4 - y * False)
print(result)


name = input("Ingresa tu nombre ")

print(f"Hola {name}")
edad = int(input("Ingresa tu edad "))
edad = edad + 1
print(edad)