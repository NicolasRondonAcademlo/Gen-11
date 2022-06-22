my_string = "This is my string!"
print(len(my_string))
print(my_string[0:4])
print(my_string[1:7])
print(my_string[8:len(my_string)])

# Obtener la ultima posicion de lagun iterable (string)
print(my_string[-1])
print(my_string[len(my_string) -1])

print(my_string[:4])
print(my_string[2:])

print(my_string[0:0:5])


# 
name = "Carla"
last_name = "Jimenez"

full_name = name + " " + last_name
print(full_name)
full_name = f"My full name is {name} {last_name}"

print(full_name)
full_name_2 = "My full name is {0} {1}".format(name, last_name)
full_name_3 = "My full name is {nombre} {apellido}".format(nombre=name, 
    apellido=last_name
    )
print(full_name_2)
print(full_name_3)

from string import Template

t = Template("Mi nombre es $nombre")
nombre = t.substitute({
    "nombre": "Nicolas"
})
print(nombre)