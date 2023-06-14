
#! Condicionales

# todo ejemplo de if, sin else

num= 5

if num == 5:
    print("Es igual a 5")  #! la identacion es IMPORTANTE, siempre 4 espacios o un tabulador.


# todo if + or, else, etc.

if num % 2 == 0 or num % 1 == 0:
    print("the number is multiple")   

if num % 2 == 0 and num % 1 == 0:
    print("the number is multiple")   

#todo if's anidados.

num2 = 63

if num2 >= 40 and num2 <= 80:
    if num2 >= 50 and num2 <=75:
        if num2 >= 50 and num2 <= 70:
            print(" num2 is in the range of 60 to 70")


# todo reasignando con ifs


if num < 10:
    num=20
    newNum=num * 2

print(num)
print(newNum)    




# ! Else if

if num < 10:
    print("num is minor than 10")
else:
    print("num is bigger than 10")    

# todo OPCION DOS DE IF ELSE


output = "the number is minor than 10" if num < 10 else "the number is bigger than 10"
print(output)


# todo ELIF


light = "red"

if light == "green":
    print("go")
elif light == "yellow":
    print("careful")
elif light == "red":
    print("stop")        
else:
    print("incorrect light sign")    