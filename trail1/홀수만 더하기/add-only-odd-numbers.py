n = int(input())
lst = [int(input()) for _ in range(n)]
sum_n = 0
for i in range(n):
    if lst[i]%2==1 and lst[i]%3==0:
        sum_n += lst[i]

print(sum_n)