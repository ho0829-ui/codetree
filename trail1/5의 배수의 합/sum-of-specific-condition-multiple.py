a, b = map(int, input().split())
sum_n = 0
if a > b:
    a, b = b, a
for i in range(a, b+1):
    if i % 5 == 0:
        sum_n += i
print(sum_n)