# The word after "for" is the loop variable.
# range(start, end) stops before the end.
# Example: range(5, 10) → 5, 6, 7, 8, 9

for ch in "Hello":
    print(ch)

for n in range(5, 10):
    print(n)

names = ["Sulaiman", "Tabasom", "Jan"]

for person in names:
    print(person)

for name in names:
    print(f"Hello {name}!")
    if name == "Sulaiman":
        print("You bastard")
        for again in names:
            print("I'm inside the if clause")
    elif name == "Tabasom":
        print("You beauty")
    else:
        print("You random")
