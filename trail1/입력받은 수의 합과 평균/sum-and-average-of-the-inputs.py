n = int(input())
lst = [int(input()) for _ in range(n)]
sum_n = 0
avg_n = 0
for i in range(n):
    sum_n += lst[i]
avg_n = sum_n/n
print(f'{sum_n} {avg_n:.1f}')