
#! Funciones

#todo Estructura basica
#  Palabra reservada + nombre + (parametros)+ cierre de kla misma :
def primerFuncion(param1,param2):
    # Instrucciones
    variable = "hola", param1,param2
# return
    return variable

# resultado = primerFuncion("verde", 8)  #? sepuede agregar lo que se quiere retornar dentro de una variable y correrla con print o se puede agregar todo en print como si fuera conole.log

# todo function + if/ else
print(primerFuncion("verde", 8)  )


def minNum (uno,dos):
    if uno > 8:
        return uno,"Es mayor a 8"
    else:
        return uno, "Es menor a 8"    

print (minNum(5,8))    


# todo function mas parametros por defecto.


def nueva (uno=2, dos=3):  #? no funciono.
    var= uno, "es mayor que ", dos
    return var
print(nueva)    