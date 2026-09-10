n = int(input())
sum_n = 0

for i in range(1, n+1):
    sum_n += i
    if sum_n >= n:
        print(i)
        break