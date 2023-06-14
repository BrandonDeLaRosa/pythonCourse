

# ! STRINGS METHODS.

# todo Primera letra en mayusc.

txt= "hola me llambo brandon"  #? Si el primer caracter es numero no cambia nada.
t= txt.capitalize()
print(t)

t2= txt.title() #? todas las palabras inician con mayusculas.
t2= txt.istitle() #? pregunta si todas las letras 1 de las palabras son masyuc.
print(t2)


# todo todas a minusc.

txt2 = "Hola Yo soy"
x= txt2.casefold()
print(x)

l= txt2.lower()
# l= txt2.upper()  <-- a mayusc (lower) a minusc
print(l)


txt3 = "pineapple"
p= txt3.center(20,'z') #? centrar la palabra entre 20 caracteres dentro de letras z.
print(p)

# todo Contar dentro de un string

txt4= 'i love watermelons,watermelons are my favorite fruit'
w= txt4.count("watermelons")
print(w) #? result 2

# todo letra con la que temrina.

e= txt4.endswith("w")
print(e)
e1= txt4.endswith("fruit", 5,100) #?  Devuelve true, esta buscando coincidencias dentro de los caracteres idicie 5 y 100(aunque no existe el 100)
print(e1)


# todo encontrar elementos en el string

fi= txt4.find('fruit')
# fi= txt4.index('fruit') <-- index es igual.
print(fi) #? Devuelve 47 <-- la palabra inicia en el inidce.. 47

loUp= txt4.isupper()  #?all in uppercase? === false
print(loUp)

# todo el elemento es numero ?

print(txt4.isnumeric())  #? False, el txt4 es puro string
z=" ".join(txt4) #? cada caracter lo divide por espacios, incluso los eespacios tambien .
print(z)
# metodos iguales que en javascript (replace, split, join)



