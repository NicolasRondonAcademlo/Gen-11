frase = "Esta es una gran frase"
name = 0 

for nombre_variable_temporal in frase[::3]:
    print(nombre_variable_temporal)


a = range(1,11,3)
for i in a:
    print(i)

print("?----")
for i in range(1,45):
    if i % 10 == 0:
        print(i)

n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

num_odd = [x for x in num_list if x%2 !=0]
print(num_odd)

nueva_lista = []
for x in num_list:
    if x%2 !=0:
        nueva_lista.append(x)

lista = [1,2,3,4]
num = 0
for pepito in lista:
    if pepito % 2 == 0:
        lista[num] = "par"
    num += 1

print(lista)

