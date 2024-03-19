#2019112148 김준호

def multiple(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

nums = [8, 2, 3, -1, 7]

print(multiple(nums))
