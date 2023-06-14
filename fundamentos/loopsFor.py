
#! Iteradores 


# todo recorrer una lista.

number_list = [1,2,3,4,5,6,7,8,9]

for number in number_list:
    print( " el munero actual es ", number)

# todo iterar de un numero a ...
for number in range(1,23):
    print(number)




maxOddNumber = 0
maxEvenNumber = 0

for number in range(1,100):
    if number % 2 == 0:
        print(f"the number{number} is even")
        maxEvenNumber = maxEvenNumber + 1
    else:
        print (f"the number {number} is odd")    
        maxOddNumber = maxOddNumber + 1

print("La cantidad de numeros pares es ", maxEvenNumber)
print("La cantidad de numeros impares es ", maxOddNumber)


# Si se quiere detener un if se usa 
# found:
# break

# O si se quiere no agregar los elementos encontrado  se coloca continue, asi sigue iterando  y dando los resultados que no son ese resultado.