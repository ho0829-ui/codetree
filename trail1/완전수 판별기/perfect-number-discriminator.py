n = int(input())
sum_n = 0
for i in range(1,n):
    if n%i==0:
        sum_n += i
if n == sum_n:
    print('P')
else:
    print('N')