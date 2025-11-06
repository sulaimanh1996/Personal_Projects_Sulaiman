# Dictionaries store key-value pairs using {}.
# Keys can be strings, ints, or floats; values can be any type.

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
print(my_info.values())
print(my_info.pop("Name"))
print(my_info)
print(my_info.get("Age"))
my_info.update({"Height": 177})
print(my_info.popitem())
print(my_info)
