# Variables store values for later use.
# You can combine (concatenate) strings or add numbers.
# You cannot add a string and an integer directly—use str() or int() to convert.
# Multiplying a string repeats it.
# f-strings make it easy to combine text and variables.

name = "bih ahh"
greeting = "Welcome"
complete_greeting = name + " " + greeting

number_1 = 1
number_2 = 2

a = 3
b = "test"

d = 3 * a  # 9
e = 3 * b  # "testtesttest"

print(complete_greeting)  # "bih ahh Welcome"
print(number_1 + number_2)  # 3
print(complete_greeting + str(number_2))  # "bih ahh Welcome2"
print(int("1") + int("1"))  # 2
print(d)  # 9
print(e)  # testtesttest
print(f"{greeting} {name}")  # "Welcome bih ahh"
print(f"{greeting} {number_1}")  # "Welcome 1"
