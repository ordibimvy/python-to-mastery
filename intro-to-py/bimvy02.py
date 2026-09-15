import random
import math
name = "Ordi"
age = 23

print("Welcome, " + name + " to our Adventure Game.")

user_id = str(math.pow(age, 1) + random.randint(1, 9999))

print("You user id is: " + user_id)

print("You are walking down the street and you get into a maze and now, you have to find your way back out of it and there are monsters and there are multiple exits to win the grand prize, go ahead and play")

print("You get to the entrance and see two doors, pick one (pick 1, 2, 3)")
player_pick1 = 1
player_pick2 = 2
player_pick3 = 3

player_pick11 = 2
player_pick12 =1

player_pick111 = 1


if player_pick1 == 1:
    print("The door opened and you can go ahead to the next door (1, 2, 3)")
    if player_pick11 == 2:
        print("You opened the door, no monsters go ahead")
        if player_pick111 == 1:
            print("You got Killed")
        else:
            print("YOU WON THE POT OF GOLD")
    elif player_pick12 == 3:
        print("You saw a monster but you killed it")
    else:
        print("YOU GOT KILLED")
elif player_pick2 == 2:
    print("YOU FOUND THE PORTAL TO THE GOLD, YOU WIN")
else:
    print("YOU GOT EATEN AND DIED")
