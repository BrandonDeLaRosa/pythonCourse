class Student:
    def __init__(self, name=None, physics=None, chemestry=None, biology=None) -> None:
        if physics > 100 or chemestry > 100 or biology > 100:
            print(" las materias no pueden ser mayores a 100 ")
        self.name = name
        self.physics = physics
        self.chemestry = chemestry
        self.biology = biology

    def total_obtained(self):
        return self.physics + self.chemestry + self.biology

    def promedio(self):
        return self.total_obtained() / 3   


brandon = Student("Brandon De La Rosa", 100,100,100)

print(brandon.total_obtained())        
print(brandon.promedio())



class Calculator:
    def __init__(self,number_1,number_2) -> None:
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        return self.number_1 + self.number_2
    def substract(self):
        return self.number_1 - self.number_2
    def multiply(self):
        return self.number_1 * self.number_2
    def division(self):
        return self.number_1 / self.number_2

firstOperation = Calculator(10,2)        

print(firstOperation.add())
print(firstOperation.substract())
print(firstOperation.multiply())
print(firstOperation.division())