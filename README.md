# Control Flow in Python

### If, else if (elif), else statements (blocks)

- If statements check to see if a condition is true and if it is true then carry it will carry out the code within.
  For example in the code below the print statement will be executed if the statement is true.
- Elif statements work the same as the if statements but will only execute if the if statement is false.
- Else statements will execute if all the statements above it are false as the conditions are not met.

```
age = 14
# if the user is above the age of 15 allow them to buy a ticket
if age >= 15:  # if this condition is met/ true the print statement will be executed
    print("Thank you, please proceed with your purchase")

# if the user is under 15 years of age do not allowed to buy a ticket
elif age < 15:
    print("Sorry you are under age to watch this movie")

# else block is executed if none of the above conditions are met
else:
    print("Oops something went wrong, please try later")

```
## Loops
Loops help to iterate through data.
- for loops 
- while loops

### For loops
- Is used to repeat a series of statements a fixed number of times (iteration).
- Can also be used to loop through an iterable object like a list.
- syntax to create a loop
- for is python keyword variable

- Iterating through items in a list
```
shopping_list = ["bread", "eggs", "milk", "orange"]

for items in shopping_list:
    print(items)
```
- Iterating through letters in a word
```
for letter in "fruits":
    print(letter)
```
- For loop including an if statement.
```
shopping_list = ["bread", "eggs", "milk", "orange"]
for items in shopping_list:
    print(items)
    if items == "milk":  # when the condition is true the loop ends
        # break is a key word
        break
        # at this point when milk is found in the items
        # iterating through the shopping_list the loop will stop
```
break stops the loop 

- Iterating through a dict.
```
food_bill = {1: {"name": "James", "bill": "£1"},
             2: {"name": "Bond", "bill": "£2"},
             3: {"name": "shah", "bill": "£3"}}

for items in food_bill.keys():
    print(items)

for items in food_bill.values():
    print(items)
```

### While loops
- Repeatedly executes a statement inside the loop as long as a given condition is true.
- Can become infinite if a condition is never false.

- what
- where
- use cases
```
# syntax while - condition  - value

num = 0
while num < 10:  # while true continue ,if false stop
    print(f"it's working -> {num}")
    num += 1

# second iteration
num = 0
while num < 10:  # while true continue ,if false stop
    print(f"it's working -> {num}")
    if num == 4:  # if true the loop ends
        break
    num += 1

# Use case as the 3rd Iteration

age = input("please enter your age")
print(f"your age is {age}")

user_prompt = True
while user_prompt:
    age = input("please enter your age")
    if age.isdigit():  # isdigit() ensures the user input is in digits
        user_prompt = False
    else:
        print("please enter your age in digits")
print(f"your age is {age}")  # this ine of code only gets executed
# if the user enters age in digits

# ensure the loop conditions are in your control to avoid going into the infinite loop
```

