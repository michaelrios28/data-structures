

products = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

print(list(map(lambda item: item[1], products)))
print([item[1] for item in products])


print(list(filter(lambda item: item[1] > 9, products)))
print([item for item in products if item[1] > 9])
