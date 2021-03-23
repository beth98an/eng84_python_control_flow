# Control flow
# Conditional statements are used to control flow of our program
# if, else if/elif, else

age = 15
# if the user is above the age of 15 allow them to buy a ticket
if age >= 15:  # if this condition is met/ true the print statement will be executed
    print("Thank you, please proceed with your purchase")

# if the user is under 15 years of age do not allowed to buy a ticket
elif age < 15:
    print("Sorry you are under age to watch this movie")

# else block is executed if none of the above conditions are met
else:
    print("Oops something went wrong, please try later")


# Exercise
# as a user I would like to sell tickets according to the age of the user
# and category of the movie
# age = 12, PG, U, 15, 18
# user input to let us know the age to decide whether to sell the ticket or not
# casting implemented
# display the age back to the user with appropriate message

age = int(input("How old are you? "))
print(age)

if age >= 18:
    print("This user is allowed to see any 18, 15, 12, PG or U rated movie")
elif age >= 15:
    print("This user is allowed to see any 15, 12, PG or U rated movie")
elif age >= 12:
    print("This user is allowed to see any 12, PG or U rated movie")
else:
    print("This user is allowed to see any U rated movie and any PG rated movie with their parents permission")
