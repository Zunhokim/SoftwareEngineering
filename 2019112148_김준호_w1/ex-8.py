# 2019112148 김준호

a = ['Red', 'Green', 'White', 'Black', 'Yellow', 'Pink', 'Blue']
b = ['Red', 'Green', 'Black', 'White', 'Yellow', 'Indigo', 'Blue']

difference = []

for item in a:
    if item not in b:
        difference.append(item)

for item in b:
    if item not in a and item not in difference:
        difference.append(item)

print(difference)
