
class ClassA:

    def  __init__(self, name:str) -> None:
        self.name = name
        self.otro = name
        pass

    def print_saludo(self ):
        print(f"Hola {self.otro}")

    def print_twice(self):
        print(f"Hola {self.otro}")
        self.print_saludo()
        return 8


class  ClassB(ClassA):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def turn_tv(self):
        print("Turn on tv")


c = ClassB("Carlos")
c.turn_tv()
c.print_saludo()