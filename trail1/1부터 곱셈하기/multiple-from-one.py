n = int(input())
mul_n = 1
for i in range(1, 11):
    mul_n *= i
    if mul_n >= n:
        print(i)
        break