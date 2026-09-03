#introduction to my mad libs game
print("Hi, Welcome to this Mad Libs Program!") # usage of strings
name = input("What is your name?: ") # usage of inputs and assignments variables

print("Welcome, " + name) 

age = int(input("How old are you?: "))
if age > 18:
    print("Okay, you are not a minor, that is a savor!")
else:
    print("You are a minor, I would be a little cautious on this one.")

bank_account = input("How much money do you have in your Bank account?: ")
print("Wow, you have $" + bank_account)

single_married = input("Do you have a girlfriend? (Yes/No)")

if single_married == "Yes":
    girlfriend_number = int(input("How many girlfriends do you have?"))
    if girlfriend_number > 1:
          print("Oh wow you are a player!!!") # print statemnet usage 
    else:
        print("great, loyalty is the policy")

print("With that being said.")
print("Since you have", girlfriend_number, "girlfriends")

balance = int(bank_account) # casting
girlfriend_number = int(girlfriend_number) # had to convert it to int (casting)
print("Then your total money share bewteen them when you divorce is", balance / girlfriend_number) # weird arithmetic but I think thats one way I couldve used it
# used division of int
print("***********************************") # intro ends, game starts

print("Alright " + name + ", now the real game. Give me some words — no peeking at why.\n")

#lets collect some information for the mad libs game
adjective_1 = input("An adjective: ")
plural_noun_1 = input("A plural noun: ")
verb_ing_1 = input("A verb ending in -ing: ")
place = input("A place: ")
adjective_2 = input("Another adjective: ")
noun_1 = input("A noun: ")
celebrity = input("A celebrity's name: ")
number = input("A number: ")
food = input("A food: ")
verb_past = input("A past-tense verb: ")
body_part = input("A body part: ")
adjective_3 = input("One more adjective: ")
animal = input("An animal (plural): ")

# okay this is our story now, sorry I am a little ahead of the class 
# I did a lot of python for the past year since I really wanted to learn it. 

story = f"""
========================================
   THE {adjective_1.upper()} DAY OF {name.upper()}
========================================

It was a {adjective_1} morning when {name} woke up surrounded by
{plural_noun_1}. Nobody knew how they got there, and weirdly nobody
was {verb_ing_1} hard enough to find out.

{name} grabbed a coat and headed straight to {place}, where the
air smelled {adjective_2} and a stray {noun_1} sat on the counter
like it owned the building.

That's when {celebrity} burst in holding {number} plates of {food}.
"I've been looking for you for {number} years!" they {verb_past}.
{name} scratched their {body_part} and said nothing, which in
hindsight was the {adjective_3} decision of the entire day.

They left together in a van driven by {number} {animal}.
Nobody has seen them since.

--------- THE END ---------
"""

print(story)
