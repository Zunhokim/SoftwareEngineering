# 2019112148 김준호

arr = [1, 3, 5, 3, 7, 1, 9, 3]
first_duplicate = -1

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            first_duplicate = arr[i]
            break
    if first_duplicate != -1:
        break

if first_duplicate != -1:
    print("First duplicate element:", first_duplicate)
else:
    print("-1")
