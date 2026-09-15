from math import floor

user_name = str(input("What is your name? ")) # doubling down on getting a string
print("Hi, " + user_name + " Welcome to our basic money management?" ) # allows us to concatenate

user_salary = float(input("What is your monthly salary? ")) # take in a float incase user puts decimals
print("Okay,", round(user_salary), "is a good estimate!") # round it up so we have something solid

user_family = int(input("How many family members do you have? "))
rent = float(input("What do you pay for your rent? (include decimals) "))
car_note = float(input("What do you pay for your car note (include decimals)? "))
food = float(input("How much do you pay for your food monthly? "))

user_balance = user_salary - (rent + car_note + food)

user_balance = floor(user_balance) # this allows user to use money and at least have some few cents remianing

print("Your remaining balance is: $",round(user_balance), ".00") # rounding balance to 2 decimal place

user_family_share = user_balance / user_family

print("You can still be generous and share equally $", round(user_family_share, 2), "with your family")


                  
