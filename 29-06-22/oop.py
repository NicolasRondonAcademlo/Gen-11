class ClassName:
    pass

# Crea - Inicializa - Destruye

# Comportamientos (metodos), Datos (propiedades)
# Roberto

class Person():

    def __init__(self, name, age, telf=None) -> None:
        self.name = name
        self.age = age

    def saluda(self): 
        return f"Hola {self.name}"

  


    
roberto = Person("Roberto", 85)
print(roberto)
print(roberto.name)
roberto.telefono = 55488
print(roberto.telefono)
print(roberto.saluda())
alberto = Person("Alberto", 85)
roberto.address = "22222"
alber_2 =  Person("Alberto", 85)

