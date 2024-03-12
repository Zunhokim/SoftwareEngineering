# 2019112148 김준호

a = (('333', '22'), ('1414', '2323'))

b = tuple(tuple(int(x) for x in tup) for tup in a)

print(b)
