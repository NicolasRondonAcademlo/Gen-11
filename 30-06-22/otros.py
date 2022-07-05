a = [{"name": "Nicolas", "score": 87}, {"name": "Andres", "score": 87}]
b = [{"name": "NicolaS", "score": 8107}, {"name": "Andres", "score": 87}]

for element in a:
    element["name"] = element["name"].lower()

for element in b:
    element["name"] = element["name"].lower()

print(a)
print(b)