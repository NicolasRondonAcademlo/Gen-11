
def funcion_a(funcion_b):
    def funcion_c():
        print("Antes de la ejecucion de la funcion a decorar")
        funcion_b()
        print("Despues de la ejecucoion de la funcion a decorar")
    return funcion_c

@funcion_a
def saludar():
    print("Hola Mundo")

saludar()