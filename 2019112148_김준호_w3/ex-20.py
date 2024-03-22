# 2019112148 김준호

N = 5

for i in range(1, N * 2):

    star = i if i <= N else 2 * N - i

    for j in range(star):
        print("*", end=" ")

    print()