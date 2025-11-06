# while repeats as long as the condition is True.
# Stops when the condition becomes False.

a = 0
while a != 10:
    a += 1
    print("1 added!")

user_input = ""
while user_input != "9":
    user_input = input("Guess a number between 1 and 10: ")
    if user_input != "9":
        print("Wrong buddy")
    elif user_input == "9":
        print("You got the right number!")
