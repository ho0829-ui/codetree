a, b = map(int, input().split())
mul_n = 1
for i in range(a, b+1):
    mul_n *= i
print(mul_n)