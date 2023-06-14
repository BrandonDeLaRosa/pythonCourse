
#! Variables 


n = 300   
print(n)   #Similar a console.log

n =1000    #?Las variables son reasignables.
print(n)

a = b = c = 400
print(a,b,c)  # Cada una de las variables (abc) reciben el mismo valor y las tres se ejecutan



# la misma variable puede tener un tipo de dato y ser cambiado.
var ="soy string"
print(var)
print(type(var)) #?Similar a typeOf

var = 123
print(var)
print(type(var))

#TODO No existen constantes 
#TODO No pudes inicializar variables con 9 o guin medio y son case sensitive.



#! DATA TYPES.



# # -NUMBERS
# # -STRINGS
# # -BOOLEANS


# #? NUMBERS INT AND FLOAT


# number_1 = 5
# print(type(number_1))    #integer
# number_2 = 5.1
# print(type(number_2))    #float
# number_3 = -5
# print(type(number_3))

# #? booleans  
# # todo Los buleanos deben inciar con mayuscula  --->"T"rue   ----> "F"alse.    Sino marca error.


# print(True)  

# print(type(True))

# false_bool= False
# (type(false_bool))



# # ! STRINGS   Son inmutables



# # TODO Las tres marcan tipo: |string

# text= "Esto es igual aun string"
# text_2 = 'Esto es un string comilla simple'
# text_3= """Comillas triples, sirven para: documentar funciones en python (docStrings)""" 

# print(type(text))     
# print(type(text_2))
# print(type(text_3))



# # !CONCATENACIONES.




# # todo OPERADOR +

# name = "Juan Jose"
# last_name = "Gomez"
# full_name= name + " " + last_name

# print(full_name)


# result = 1 + 2
# print(result)

# # textErr= "El resultado de 1 + 2 es:" + result   #todo <--- Esto marca error porque no se pueden concatenar strings con enteros.

# texto = "El resultado de 1 + 2 es igual a:" + str(result) #todo Este si es correcto, el metodo str === .toString()
# print(texto)

# #TODO OPERADOR %

# name2 = "Academlo"
# my_name = "es Brandon"
# frase = "Hola %s, mi nombre %s" % (name2, my_name)   #? el simbolo "%s", sera reemplazado por lo que se encuentre en la variable name2, y el segundo "%s" sera reemplazado por lo que hay en 2da variable.
# print(frase)


# #TODO MEDOTO FORMAT

# lin = "Estoy aprendiendo"
# lin2 = "python"

# fraseConca = "{} {}".format(lin, lin2)  #? Si se dejan vacias las llaves tomara las variables en el orden que estan en (). Si pongo primero lin2 y despues lin === python Estoy aprendiendo.
# fraseConca2 = "{1} {0}".format(lin, lin2) #? Puedo organizarlas tomando el indice de fromat, si en las llaves pongo indice 0 y 1. Ordenandolas como yo decida.
# fraseConca3 = "{lang} {var_apren}".format(var_apren = lin, lang = lin2)  #? O puedo nombrar los objetos y asignarlos "=" dentro del metodo format
# print(fraseConca)
# print(fraseConca2)
# print(fraseConca3)

# #todo F-STRING


# food= "pasta"
# name3 = "lupe"
# fraseC = f"La comida favorita de {name3} es {food}"  #? NO OLVIDAR LA "f", al inicio del string
# print(fraseC)


# #todo Metodo JOIN.


# cadena = ["hola", "soy", "metodo join"]
# fraseCon = " ".join(cadena)  #? el primer elemento (" "), es lo que se a colocar entre los elementos del arreglo o lista en python
# print(fraseCon)


# # ! STRINGS, INDEX Y LENGHT



# random = "Hello"   #? El index y longitud es igual que en js
# print(len(random))    #? Cantidad de letras en un string (5)

# # TODO hello
#     #  01234   <--- indices
#     #        1 2 3 4 5   <---- Longitud (Se extrar con len())
#     # TODO   h e l l o
#     #       -5-4-3-2-1   <---- Si quiero acceder a los indices de cada letra 


# print(random[-1])   #? <---- mandar a consola la letra "o"


# print(len(random)-1) #? <--- Extraer ultimo valor (Igual que en js pero diferente sintaxis.)


my_string = "This is my string"
print(my_string[0:9])   #? Va devolver "this", el valor 0 si lo cuenta y el segundo valor "4", lo usa para cortar la cadena pero no develve ese indice, sino uno menos.
print(my_string[5:len(my_string)]) #? len( ) para determinar el ultimo caracter y hacer un slice raro
print(len(my_string))
print(my_string[0:7:2])  #? el valor tres del "arreglo", nos dice de cuantos caracteres es el avance al siguiente caracter.
print(my_string[8:]) #? Le digo donde inicial, no donde terminar(TRAE EL RESTO DEL STRING)
print(my_string[:1]) #? Le indico donde termina pero no donde empieza ( Trae desde el primer caracter.)
print(my_string[::-1])  #? reverse Method in python