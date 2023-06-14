
# ! DICTIONARY

# Son objetos en python.

{
    "key":"value"
}


# ! CREATE DICTIONARIES.


#todo opcion 1  LA MAS USADA Y RAPIDA.
phoneBook = {
    "batman": 45678,
    "Cersi": 422,
    "GhostBuster": 2345
}
print(phoneBook)

emptyDict= dict()  #? empty Dcit


# todo opcion2
phoneBook2= dict(
    batman= 234455, cersei=34556, javascript="Igual a un objeto"
)


# todo opcion3
phoneBook3 = dict(
    [
    ("batman", 45678),
    ("Cersi", 422),
    ("GhostBuster", 2345)
    ]
)

print(phoneBook2)

# !aCCESING DICTIONARIES    (los dictionaries no tienen orden)



# TODO ACCEDER A VALORES DENTRO DE DICCIONARIOS

batman_number = phoneBook["batman"] 
print(batman_number)  #? Devulve el valor guardado en es parametro 
print(phoneBook.get("Cersi")) #? Opcion 2


#todo  Añadir un nuevo elemento y valor momentaneamente.

print(phoneBook.get("Andrea", 957483))
print(phoneBook)




# ! OPERACIONES EN DICTIONARIES.

myDict = {
    "key": 4,
    "ke2": ["hola","Academlo"],
    "ket3": {
        "a":1,
        "b":2
    }
}


#todo  Añadir un nuevo elemento y valor permanentemente.


phoneBook["godzilla"] = 12345
print(phoneBook)  #? Elementos agregados a dictionary


phoneBook["godzilla"] = 75892375082 #? reasignacion


# todo Eliminando elementos.

del phoneBook ["batman"] 
print(phoneBook) 

cersi = phoneBook.pop("Cersi")
print(phoneBook)  #? Eliminando por nombre de elmento.


#todo Longitud del dictionary

print(len(phoneBook))  #? Devuelve dos pues solo hay dos elementos.

lenPhoneBook= len(phoneBook)
print(lenPhoneBook)  #? opcion 2

# todo Cheking existance

print("batman" in phoneBook)  #? false
print("godzilla" in phoneBook)  #? True


# todo updating/mergin dictionaries.

second_Phone_Book = {
    "catWoman": 213432,
    "hulk": 4211345,
    "wolverine": 47802
}

phoneBook.update(second_Phone_Book)   #? Elementos agregados a phonebook

print(phoneBook)