
class Rectangulo:
    def __init__ (self,width,heigth) -> None:
        self.__width = width
        self.__heigth = heigth

    def area(self):
        return self.__width * self.__heigth  
    
    def perim(self):
        return (self.__width + self.__heigth) * 2    

producto = Rectangulo(5,4)

print(producto.area())
print(producto.perim())