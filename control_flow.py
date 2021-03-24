# # Control flow
# # Conditional statements are used to control flow of our program
# # if, else if/elif, else
#
# age = 15
# # if the user is above the age of 15 allow them to buy a ticket
# if age >= 15:  # if this condition is met/ true the print statement will be executed
#     print("Thank you, please proceed with your purchase")
#
# # if the user is under 15 years of age do not allowed to buy a ticket
# elif age < 15:
#     print("Sorry you are under age to watch this movie")
#
# # else block is executed if none of the above conditions are met
# else:
#     print("Oops something went wrong, please try later")
#
#
# # Exercise
# # as a user I would like to sell tickets according to the age of the user
# # and category of the movie
# # age = 12, PG, U, 15, 18
# # user input to let us know the age to decide whether to sell the ticket or not
# # casting implemented
# # display the age back to the user with appropriate message
#
# age = int(input("How old are you? "))
# print(age)
#
# if age >= 18:
#     print("This user is allowed to see any 18, 15, 12, PG or U rated movie")
# elif age >= 15:
#     print("This user is allowed to see any 15, 12, PG or U rated movie")
# elif age >= 12:
#     print("This user is allowed to see any 12, PG or U rated movie")
# else:
#     print("This user is allowed to see any U rated movie and any PG rated movie with their parents permission")


# syntax to create a loop
# for is python keyword variable then data_collection

shopping_list = ["bread", "eggs", "milk", "orange"]
print(shopping_list)
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])

# Let's for loop to iterate through out list
for items in shopping_list:
    print(items)

# Let's iterate through letters in a word
for letter in "fruits":
    print(letter)

shopping_list = ["bread", "eggs", "milk", "orange"]
for items in shopping_list:
    print(items)
    if items == "milk":  # when the condition is true the loop ends
        # break is a key word
        break
        # at this point when milk is found in the items
        # iterating through the shopping_list the loop will stop

# Let's create a dict of our food bill so we can iterate through it using a for loop
food_bill = {1: {"name": "James", "bill": "£1"},
             2: {"name": "Bond", "bill": "£2"},
             3: {"name": "shah", "bill": "£3"}}

# Let's iterate through our dict
for items in food_bill.keys():
    print(items)

for items in food_bill.values():
    print(items)

# print the names with the bill
for items in food_bill.values():
    print(items["name"] + " " + items["bill"])






