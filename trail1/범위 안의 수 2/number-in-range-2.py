lst = [int(input()) for _ in range(10)]
sum_n = 0
cnt = 0
avg_n = 0

for i in range(10):
    if lst[i]>=0 and lst[i]<=200:
        sum_n += lst[i]
        cnt += 1
avg_n = sum_n / cnt
print(f'{sum_n} {avg_n:.1f}')