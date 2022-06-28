

def nombre_funcion(arg_1, arg_2):
    print(f"El argumento 1 {arg_1}")
    print(f"El argumento 2 {arg_2}")
    name = "Guillermo"
    return f"La edad de {name} es {arg_1 + arg_2}"


a = nombre_funcion(1,2)

def suma(a:int,b:int) -> int:
    print(a)
    print(b)
    return a +b 

b = suma(7.0,8)
print(b)

c= suma(b=98, a=38 )
print(c)


def suma(a:int=10, b:int = 10, c:int = 10 ) :
    return a +b +c

d = suma(5,5,5)


def amigo(a:int=5):
    a +=5
    print(a)
    return 

amigo()
amigo()
amigo()

def f(my_list=None):
    # Los parametros por defecto son definidos una unica vez en python
    if not my_list:
        my_list = []
    my_list.append("###")
    return my_list


def suma(*args:tuple[int]) -> int:
    suma = 0
    for number in args:
        suma = suma + number
    return int(suma)

z = suma(8,9,10)
print(z)
z = suma(8,9,10,10)
print(z)
z = suma(8,9)
print(z)
# packing tuples
# packing dictionaries

values = {
    "name": "Luis",
    "cellphone": 65446446,
    "age": 41
}

def show_info(**kwargs):
    user = kwargs.get("name", "Sin Nombre")
    age = kwargs.get("age", 0)
    cel = kwargs.get("cellphone", 0000)

    return f"El usuario {user} tiene una edad de {age} y su celular es {cel} "

a = show_info(**values)
print(a)

values = {
  
}
a = show_info(**values)
print(a)

def  enter_users(quantity:int)-> dict:
    """Ingresa Usuarios

    Args:
        quantity (int): cantidad de usuarios a ingresar

    Returns:
        dict: lista de de usuarios
    """
    value = []
    for i in range(quantity):
        name = input("Ingresar tu nombre ")
        value.append({"name": name})
    return value


from typing import List
def make_coffe(users:List[dict]) -> List[str] :
    """Esta funcion se encarga de hacer cafe para todos

    Args:
        users (List[dict]): Lista de usuarios a tomar cafe

    Returns:
        List[str]: Usuarios con su cafe
    """
    for user in users:
        print(f"Un cafe para {user['name']}")

users = enter_users(8)
cofee = make_coffe(users)
cofee = make_coffe(enter_users(1))