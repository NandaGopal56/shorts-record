fruits = ("apple", "banana", "cherry")

first, second, third = fruits

print(first, second, third)


first, *rest = [12, 33, 122, 45]
print(first, rest)


first, *rest, last = [42, 771, 256, 1337]
print(first, rest, last)
