class ClassName:
    pass

# Crea - Inicializa - Destruye

# Comportamientos (metodos), Datos (propiedades)
# Roberto

class Person():

    def __init__(self, name, age, telf=None) -> None:
        self.name = name
        self.age = age
        self.telf = telf
        print(self.saluda())

    def saluda(self): 
        return f"Hola {self.name}"

  


    
roberto = Person("Roberto", 85, 8897779)

# Empresa 
# Empleado
# Trabajo
# Vehiculo

class Empresa:
    country = "Colombia"

    def __init__(self, name:str, addres:str) -> None:
        self.name = name
        self.addres = addres

    def do_contract(self, employe):
        print(f"Se contracto a {employe} en la empresa {self.name}")

academlo = Empresa("academlo", "calle muy lejos")
academlo.do_contract("Luis")