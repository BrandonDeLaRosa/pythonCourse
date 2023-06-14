class employee:
    def __init__ (self,id=None, salary=None, department=None) -> None:
        self.id = id
        self.salary = salary
        self.department = department

    def tax(self):                #? Un metodo es una funcion reutilizable desntro de una clase 
        return self.salary * 0.2

    def salary_per_day(self):   
        return self.salary / 30    

    def demo(self):
        pass     

pepe = employee(145,2000, "HR")


print(pepe.salary)
print (pepe.tax())

print(pepe.salary - pepe.tax())

print(pepe.salary_per_day())