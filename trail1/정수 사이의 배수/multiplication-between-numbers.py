a, b = map(int, input().split())
sum_n = 0
avg_n = 0
cnt = 0

for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sum_n += i
        cnt += 1
avg_n = sum_n / cnt

print(f'{sum_n} {avg_n:.1f}')