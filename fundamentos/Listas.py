
# ! LISTAS 
# Las listas son arreglos de javascript.
# de igual forma tienen indice y longitud 

lista = ["Hola soy lista", 45, ["argentina,brasil,peru"], 4.5]

lista[2] = "Cambio de valor"
lista[1] += 5
print(lista)


# ! funcion range()
# Va devolver una secuencia de un numero a otro.

# todo Rango de numeros. (devuelve un array de nuemeros)
numSequ = range(0,10)
numSequ = list(numSequ) #? Aqui se agrega lo que hay en la primera seq y se realiza un listado [0,1,2,3,4,5,6,7,8,9,10]
print(numSequ) 


#todo rango de numeros y recorrerlos de 3 en tres
numSequ = range(3,20,3)
print(list(numSequ))


# todo busqueda dentro de listas
worldCupWinners = [
    [2006,'Italy'],
    [2010,'Spain'],
    [2014, 'Germany'],
    [2018, 'France'],
]

winner = worldCupWinners[0][1]  #? ITALY
print(winner)


# todo  Merging two lists

partA=[1,2,3,4]
partB=[5,6,7,8]

mergeTwoLists = partA+partB
print(mergeTwoLists)


# todo merging lists, numbers from b into a.

partA.extend(partB)
print(partA)

# todo merge and length

print(len(partA))





# ! OPERACIONES EN LISTAS
# todo agregar elelemtnos uno a uno

addElements = []

addElements.append(1)
addElements.append(2)
addElements.append(3)
addElements.append("hi")
print(addElements)


# todo cambiar elementos dentro de lista (Agregar, seleccionando el indice donde se va colocar )

changeElements = [1,2,3,5]
changeElements.insert(3,4)   #? agrega en el indice 3 el numero 4
print(changeElements)


#todo delete elements

house= ["griffindor", "Slitherin", "Ravenclaw", "Hufflepuff"]
lastHouse = house.pop()
print(lastHouse) #? Devuelve solo el ultimo elemento de la lista ("hufflepuff")

house.remove("griffindor")
print(house) #? Ya solo trae dos porque ya se elimino huff.. en la variable anterior y ahora se elimina el primero, ahora da como resultado solo [slit.. y raven..]


# todo  REVERSE
numList2 = [1,2,3,4,5]
numList2.reverse()
print(numList2)


# TODO LIST sLICING


numList3 = [1,2,3,4,5,6]
print(numList3[::-1])   #? OTRO METODO PARA REVERSE.

print(numList3[1:5]) #? Imprime todo lo que hay entre num 2 y 5


# todo buscar indice dentro de elementos de un array


lista2= ["Mexico","Paris","corea"]
print(lista2.index("Mexico"))  #? Su indice es el 0


# todo saber si un elemento esta en la lista 

print("Mexico" in lista2)  #? devuelve true, pues si esta


# todo Orden de mayor a menor en lista (numeros)
lista3= [8,9,2,5,3,7,6]
lista3.sort()
lista3.sort(reverse=True)  #?<--- Los ordena y despues en reversa mayor a menor

print(lista3) #?Devuelve el orden del array
