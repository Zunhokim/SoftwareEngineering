# 2019112148 김준호

array = ('i', [1, 3, 5, 3, 7, 1, 9, 3])

a = array[1]
a.reverse()

array = list(array)
array.pop()
array.append(a)
array = tuple(array)

print(array)