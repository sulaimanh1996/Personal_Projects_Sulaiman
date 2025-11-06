# Lists are ordered collections that can hold any data type.
# Create a list with [], and separate items with commas.
# Indexing starts at 0. You can nest lists within lists.

a = [10, 1, 2, 3, 4, 3.56, "Hello", 10]
b = []

print(a.index(10))  # Index of first 10 → 0
a.reverse()          # Reverse in place
a.pop(1)             # Remove item at index 1
a.append(99)         # Add 99 to the end
print(a.count(10))   # Count how many times 10 appears

b = a.copy()         # Make a shallow copy
a.clear()            # Remove all items
a.extend(b)          # Add all items from b
a.insert(0, 1)       # Insert 1 at the start

print(a)  # Show current list a
print(b)  # Show copied list b

a += [45, 67, 77, "Sulaiman"]  # Add multiple values
print(a)

a = [10, 1, 10, 2, 3, 4, 3.56, "Hello", [34, 56]]
print(a[8][1])  # Access nested list → 56
