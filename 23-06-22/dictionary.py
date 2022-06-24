phone_bok = {
    "name": "Batman",
    "city": "Ghotham",
    "cel": 545465,
    "enemy": "Himself",
    "meta": {
        "record": 1
    }
}

name = phone_bok["name"]
cel = phone_bok["cel"]
print(name, cel)
print(phone_bok["meta"]["record"])

empty_dict = dict()
empty_dict_2 = {}


empty_dict.update(
    {"color":"red"}
)

empty_dict_2.update(
    {"color":"blue"}
)
empty_dict_2.update(
    {"size":"m"}
)

print(empty_dict)
print(empty_dict_2)


empty_dict["adress"] = "Muy lejos"
print(empty_dict)

empty_dict["adress"] = "cerquita"
print(empty_dict)

del empty_dict["adress"]
print(empty_dict)

z = {'color': 'red', 'adress': 'Muy lejos', "verde": (8,)}
print(list(z.keys()))
print(list(z.values()))
print(list(z.items()))

a = z.get("color")
b = z["color"]
print(a)
print(b)

a = z.get("pepito", "NAN")
print(a)