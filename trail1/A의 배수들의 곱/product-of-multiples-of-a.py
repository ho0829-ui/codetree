a, b = map(int, input().split())
mul_n =1

for i in range(1, b+1):
    if i % a == 0:
        mul_n *= i
print(mul_n)