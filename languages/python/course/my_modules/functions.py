# by placing it here it can become a module

name="Sulaiman"
class Test:
    a = 55

def greeting_9():
    print("Hello World!")

# Functions can take parameters.
def greeting_9_with_name(name):
    print(f"Hello {name}!")

# Example: A simple guessing game function
def game_1(secret_number, stop_chars):
    user_input = ""
    while user_input != stop_chars:
        user_input = input("\nGuess a number between 1 and 100: ")
        if user_input == secret_number:
            print("You got the right number!")
        elif user_input == "stop":
            print("You wanted to stop.")
            break
        else:
            print(f"You guessed {user_input}. That's not it!")

