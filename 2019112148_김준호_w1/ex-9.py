# 2019112148 김준호

a = [(10, 20, 30), (40,50,60), (70,80,90)]

b = list(a[2])
b.pop()
b.append(100)
b = tuple(b)

a.pop()
a.append(b)

print(a)