# capitalize - > Convertir el primer caracter a mayuscula
title = "esto es una gran clase"
nuevo =title.capitalize()

# Casefold -> En minusculka
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# lower 
txt = "Hello, And Welcome To My World!"
x = txt.lower()
print(x)

z = txt.lower().capitalize()
print(z)

# upper
txt = "Hello, And Welcome To My World!"
x = txt.upper()
print(x)

# title
new = "En Peru las empandas son horneadas son"
new = new.title()
print(new)

# count
count = new.count("Son")
print(count)

# find
txt = "Hello, welcome to my world. welcome"
x = txt.find("welcome")
print(x)

# endwith
txt = "Hello, welcome to my world. "
x = txt.endswith(".")
print(x)

# startswitrhd
txt = "Hello, welcome to my world. "
x = txt.startswith("H")
print(x)

# center
txt = "banana"
x = txt.center(20, "E")
print(x)



# zfill
factura = "15"
x = factura.zfill(10)
print(x)

# split
txt = "welcome to the jungle"
x = txt.split()
print(x)

# join
x = " ".join(x)
print(x)



