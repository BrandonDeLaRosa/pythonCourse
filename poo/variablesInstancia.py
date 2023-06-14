
#! Variables de instancia y clase.

# variables de clase : que son compartidas por todos los objetos de la clase.
# variables de instancia: variables que son unicas por cada instancia.


class Player:
    team_name = "portugal"   #? Esta es una variable de clase y se comparte para todos
    team_members = []  #? variable donde se guardaran todos los nombres del equipo


    def __init__ (self,name) -> None:
        self.name = name
        self.team_members.append(self.name)   #? con esta linea agregamos cada valor encontrado a la lista.



player1 = Player("Cristiano Ronaldo")  #? Variable de instancia, unica para cada una.
player2 = Player("pepe")

print("Team members: ", Player.team_members)  #? aqui se esta utilizando una variable de clase donde ya se asignaron todos los nombres creados anteriormente


print("Name: ", player1.name)
print("team name: ", player1.team_name)


print("Name: ", player2.name)
print("team name: ", player2.team_name)

