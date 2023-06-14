
# !Getters Setters

#* Getter es un metodo que permite leer el valor de una propiedad
#* Setter es un metodo qque permite modificar el valor de una propiedad

class User:
    def __init__(self, username=None) -> None:
        self.__username = username

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username        


class User:
    def __init__(self, username=None) -> None:
        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username               


mario = User("Mario")   

print("antes del setting", mario.get_username())
mario.set_username("Pepito")  #? Aqui se reasigna el vamor agreado cuando se creo la variable mario.
print("Despues del setting", mario.get_username())  


