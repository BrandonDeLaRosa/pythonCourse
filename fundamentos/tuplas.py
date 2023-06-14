
#!TUPLAS.
# muy similar a una lista pero sus elementos son inmutables, puede tener de todo tipo de elementos, si hay una lista dentro de tupla los elementos de esta si se pueden cambiar.

# TODO ESTRUCTURA DE TUPLAS.

car = ("Ford",) #? Si la coma esto no es una tupla. 

car= ("ford","raptor,2019","red",[1,2,3])

car[-1][1] =7 #? El dos cambia a 7, aqui si se puede aditar.

hero1= ("Superman","batman")
hero2= ("ironman","spiderman")
heroes = hero1 + hero2
print(heroes)   #? Tuplas can be merged.

print("venom" in heroes)  #? se puedn hacer busquedas en las tuplas
print( hero1.index("Superman") ) #? nos arroja el indice dentro de la tupla.
