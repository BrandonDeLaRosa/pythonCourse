class employee:                     
    id = 5432
    salary = 10000
    department = 'tec'


carlos = employee()  #? <-- De esta forma se relaciona el objeto clarlos con la clase employee(que tambien es un objeto, pero sirve como plantilla.)
print(carlos.department)   #? Con punto accedemos a las propiedades.

#todo reasignando valores dentro de objetos.

carlos.salary = 10
print(carlos.salary)  


andrea=employee()
print(andrea.salary)


# todo Crear un campo que no existe en laplantilla.

andrea.title= "Manager"
print(andrea.title)


class employee:                                              #? Inicializador
    def __init__(self,id:int,salary:int,department:int) -> None:
        """
        Arguments :

            id: int - identificacion del empleado
            salary: int - salario que percibe el empleado.
            department: str - Departamento del empleado
        """
        self.id = id
        self.salary = salary
        self.department = department

peter = employee(1235, 5432, "marketing")        
michelle = employee(1235, 5432, "hr")
print(peter.department)
print(michelle.department)