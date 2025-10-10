## print
# print shows input in terminal

print ("Hello World!")

## types of inputs
# string - text used with " " or ' '
# string + strings adds it together

print ( "9" + "10 ")

# integer (int) is a rounded number
# integer + integer is sum of two integers

print ( 9 + 9 )

# float is number with decimal
# you can add float to integer

print ( 9 + 9.5 )

## math operations
# normal formulas follow the math rules
# adding () will change that like in math

print ( 9 * 9 - 5)
print ( 9 * (9 - 5))

## variables
# you can add them as strings or as int
# you cant add string with int normally
# if you add str you turn a int to a str
# if you 
# you can mutliply int and str with themselves
# f string adds multiple things together including str and int without issue into a sentence

name = ("bih ahh")
greeting = ("Welcome!")
complete_greeting = ((name)+(" ")+(greeting))
number_1 = ( 1 )
number_2 = ( 2 )
a = ( 3 )
b = ( "test" )
d = ( 3 * (a) )
e = ( 3 * (b) )

print (complete_greeting)
print ((number_1)+(number_2))
print ((complete_greeting)+(str(number_2)))
print (d)
print (e)
print (f"{greeting} {name}")
print (f"{greeting} {number_1}")
