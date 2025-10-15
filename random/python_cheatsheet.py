# ===========================
# 🐍 PYTHON CHEAT SHEET
# ===========================

## print
# The print() function shows output in the terminal.
print("Hello World!")

# ---------------------------

## types of inputs
# String: text written inside quotes (" " or ' ')
# Adding strings together combines them.
print("9" + "10")

# Integer (int): a whole number
# Adding integers gives their mathematical sum.
print(9 + 9)

# Float: a number with decimals
# You can add integers and floats together.
print(9 + 9.5)

# ---------------------------

## math operations
# Standard math rules apply.
# Parentheses () change the order of operations.
print(9 * 9 - 5)
print(9 * (9 - 5))

# ---------------------------

## variables
# Variables store values that can be used later.
# You can combine (concatenate) strings or add numbers.
# You can’t add a string and an integer directly — convert using str() or int().
# Multiplying strings repeats them.
# f-strings allow combining text and variables easily.

name = "bih ahh"
greeting = "Welcome"
complete_greeting = name + " " + greeting

number_1 = 1
number_2 = 2

a = 3
b = "test"

d = 3 * a      
e = 3 * b      

print(complete_greeting)                   
print(number_1 + number_2)                 
print(complete_greeting + str(number_2))   
print(int("1") + int("1"))
print(d)                                   
print(e)                                   
print(f"{greeting} {name}")                
print(f"{greeting} {number_1}")            

# ---------------------------

## user input
# input() enables you to input a variable value.
# Always ends with storing the input in a variable.

#? user_name = input("What is your username? ")
#? print(f"{greeting} {user_name}")

# ---------------------------

## booleans
# True or False
# == equal to
# >= greater or equal to
# <= lesser or equal to
# != not equal to
# Capital letters matter
# < less than
# > greater than

print(10 == 10)
print("S" == "s")
print("Simon" < "Simon")
print("Simon" < "simon")

# ---------------------------

## conditional statements
# if: executes only if the condition is True
# else: executes if the condition above is False
# while: repeats as long as condition stays True
# elif: adds more conditions (used between if and else)
# You can’t stack two ifs or two elses under the same block.

a = 2
b = 3

if a < 10:
    print("more!")
else:
    print("that's enough")

while a != 10:
    print("add + 2")
    a += 2

if b == 10:
    print("strong boi!")
elif b == 9:
    print("mid boi")
elif b <= 8:
    print("weak boi")
else:
    print("error: too weak")

# ---------------------------

## boolean logic
# and/or operators let you chain conditions.
# Use parentheses () to control order of operations.

a = 3
b = 4

print(a == 3 and b == 4)
print((a == 3 or b == 5) and b == 5)  # False, calculates () first
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

print(a == 3 or b == 8)
print(True or False)    # True
print(True or True)     # True
print(False or False)   # False

# ---------------------------

## lists
# Make a list with []
# If you add nothing, it’s an empty list. Separate items with commas.
# Lists are ordered and can hold different data types.
# You can put lists inside lists (nested lists).
# Count starts at 0.
# += adds elements to the list.
# -= doesn’t exist — use remove() or pop() instead.

a = [10, 1, 2, 3, 4, 3.56, "Hello", 10]
b = []

print(a.index(10))  # Returns the location of the first matching value
a.reverse()         # Reverses the list
a.pop(1)            # Removes the item at index 1 (if empty, removes last item)
a.append(99)        # Adds a value at the end
print(a.count(10))  # Counts how many times a value appears

b = a.copy()        # Copies the content of the list
a.clear()           # Clears all items
a.extend(b)         # Extends list with items from another list
a.insert(0, 1)      # Inserts a value at a specific position

print(a)
print(b)

a += [45, 67, 77, "Sulaiman"]  # Adds multiple values to list
print(a)

a = [10, 1, 10, 2, 3, 4, 3.56, "Hello", [34, 56]]
print(a[8][1])  # Finds value in a nested list (8 is where the list is, 1 is index inside it)

# ---------------------------

## Tuple
# Make a tuple with ()
# Very similar to a list, but immutable (cannot be changed)
# You can store any data type inside.
# Useful for fixed data that should not be modified.

a = (23, 45.56, "Hello", [23, "Het"], (23, 90))
print(a)

# ---------------------------

## Dictionaries
# Similar to a list, but with key-value pairs.
# Made with {} and formatted as "key": value.
# Keys can be strings, integers, or floats.
# Values can be anything (string, list, tuple, etc.)

a = {
    "name": "Sulaiman",
    "lastname": "Hashimi",
    "age": 23,
    "height": 177,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dictionary": {"dictionary1": "input1", "dictionary2": "input2"}
}

print(a)

my_info = {"Name": "Sulaiman", "Age": 29}

print(my_info)
print(my_info.values())            # Shows only values
print(my_info.pop("Name"))         # Removes given key and its value
print(my_info)
print(my_info.get("Age"))          # Returns the value of a given key
my_info.update({"Height": 177})    # Adds or updates a key-value pair
print(my_info.popitem())           # Removes the last key-value pair
print(my_info)

# ---------------------------

## For loops
# The word after "for" can be anything.
# range() prints a sequence of numbers — it stops before the end number.
# Example: range(5,10) → 5,6,7,8,9

for item in "Hello":  # Loops through each letter
    print(item)

for item in range(5, 10):
    print(item)

names = ["Sulaiman", "Tabasom", "Jan"]

for thiscanbeanything in names:
    print(thiscanbeanything)

for name in names:
    print(f"Hello {name}!")
    if name == "Sulaiman":
        print("You bastard")
        for name in names:
            print("I'm inside the if clause")
    elif name == "Tabasom":
        print("You beauty")
    else:
        print("You random")

# ---------------------------

## While loops
# while runs as long as the condition is True.
# Stops when condition becomes False.

a = 0
while a != 10:
    a += 1
    print("1 added!")

user_input = ""
# Example game that repeats until you enter "9"
while user_input != "9":
    user_input = input("Guess a number between 1 and 10: ")
    if user_input != "9":
        print("Wrong buddy")
    elif user_input == "9":
        print("You got the right number!")

# ---------------------------

## Functions
# Start with "def"
# Give your function a name followed by ()
# Code inside runs when you call it later.
# print() is also a function (built-in)
# Use parameters to pass data into the function.
# "\n" adds an empty line in print.

def greeting_9():
    print("Hello World!")

greeting_9()

def greeting_9(name):
    print(f"Hello {name}!")

greeting_9(name=input("What is your name? "))

# Example game function with parameters
def game_1(secret_number, user_input, stop_chars):    
    while user_input != stop_chars:
        user_input = input("\n\nGuess a number between 1 and 100: ")
        if user_input == secret_number:
            print("You got the right number!")
        elif user_input == "stop":
            print("You wanted to stop.")
        else:
            print(f"The number is {user_input}. You got the wrong number, buddy!")

game_1(
    secret_number=input("Fill in your guessing number: "), 
    user_input='',
    stop_chars="stop"
)

# ---------------------------
## Returning values from functions
# Use "return" to send values back from a function.
# You can return multiple values separated by commas.
# Function annotations can describe data types.

a = 'hi'
b = 45

def sum_and_product_of(a: int, b: int) -> int:
    return a + b

c = sum_and_product_of("Hi", " There")
print(c)
