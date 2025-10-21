# Use return to send a value back to the caller.
# You can also add type hints (annotations).

def sum_of(a: int, b: int) -> int:
    return a + b

result = sum_of(5, 7)
print(result)
