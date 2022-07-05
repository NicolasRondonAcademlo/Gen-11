
class Register():
    def __init__(self, username, password) -> None:
        self.username = username
        self.__password = password
        self.__age = 87

    @property
    def age(self):
        return self.__age +2

    @property
    def password(self):
        return 

    @password.setter
    def password(self, password):
        password = password.upper()
        self.__password = password

    def login(self, username, password):
        if self.username == username and self.__password == password:
            return f"{self.username} se logueo con exito"
        return f"Credentials invalid"


user = Register("Luis", 54877)
result = user.login("Luis", 54877)
print(result)
user.password = "pepito"
result = user.login("Luis", "PEPITO")
print(user.age)
print(result)
