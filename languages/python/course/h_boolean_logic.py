# Use and / or to combine conditions.
# Parentheses () control evaluation order.

a = 3
b = 4

print(a == 3 and b == 4)  # True
print((a == 3 or b == 5) and b == 5)  # False (parentheses evaluated first)
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False

print(a == 3 or b == 8)  # True
print(True or False)  # True
print(True or True)  # True
print(False or False)  # False
