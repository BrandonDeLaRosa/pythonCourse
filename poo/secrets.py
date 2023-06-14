
#! Information hiding


class People:
    def __init__(self,name, last_name) -> None:
        self.name= name
        # todo creacion de variable de clase con encapsulamiento privado.
        self.__last_name: last_name

obj_1 = People("Sandra", "Lopez")
print(obj_1.name)    
print(obj_1.__last_name)  #? Retorna un error porque no puede ser accedido a esa variable, estando fuera de la clase.





class BankAccount:
    def __init__(self, balance = 0) -> None:
        self.balance = balance = 0

    def __allow_withdraws(self):
        if self.__balance < 1:
            return false
        return true

    def deposit(self,amount):
        self.balance += amount            

    def withdraw(self, amount):
        allow = self.__allow_withdraws()
        if allow:
            self.balance -= amount

    def get_balance(self):
        return self.balance            

bbva = BankAccount()
bbva.deposit(5000)