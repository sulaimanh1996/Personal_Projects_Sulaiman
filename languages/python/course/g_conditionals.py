# if: run only if condition is True
# elif: more conditions (between if and else)
# else: runs if nothing above matched
# while: repeats as long as condition stays True
# Only one else per if-chain; multiple elif are fine.

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
