jon_snow = [
    "Jon snow",
    "Winterfell",
    30
]
print(jon_snow)
print(type(jon_snow))

print(jon_snow[-1])
 
jon_snow[2] += 3
print(jon_snow)

world_cup_winners = [
    [2006, "Italy"], 
    [20210,"Spain"],
    [2014, "Germany"],
    [2018, "France"]
]
print(world_cup_winners)
print(world_cup_winners[0][-1])

part_a = [1,2,3,4,5]
part_b = [6,7,8,9,10]

merged_list = part_a + part_b
print(merged_list)

part_a = [1,2,3,4,5]
part_b = [6,7,8,9,10]

print(part_a)
part_a.extend(part_b)
print(part_a)

num_list = []
num_list.append(1)
num_list.append(2)
num_list.append(3)
num_list.append([4,5,8])
print(num_list)

num_list = [1, 2, 3, 5, 6]
num_list.insert(3,4)
print(num_list)

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house =  houses.pop(2)
print(last_house)
print(houses)
name = "Hufflepuff"
houses.remove( name)
print(name)
print(houses)

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])


cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("London"))
print("Paris" in cities)
print("Bucaramanga" in cities)

num_list = [20, 40, 10, 50.4, 30, 100, 5,7,40]
num_list.sort(reverse=True)
print(num_list)

num_list = list(set(num_list))
print(num_list)

z = ["a", "l", "b", "q", "p"]
z.sort(reverse=True)
print(z)

lista = []
for i in [4,2,8,10]:
    lista.append(2*i)
print(lista)

lista = ["Hola", "Como", "Estas"]
txt = " ".join(lista)
print(txt)

lista = [0,1,2,3]
lista[-1] = "Hola"
print(lista)

a  = "Hola Como Estas"
z = a.split(" ")

car = ("Ford", "Raptor", 2019, "Red", (8,8))
for i in car:
    print(i)

print("Ford" in car)

a = (8,)
print(type(a))

