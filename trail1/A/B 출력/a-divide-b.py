a, b = map(int, input().split())
x = a//b
y = a%b
print(f'{x}.', end='')
for _ in range(20):
    x = (y*10)//b
    y = (y*10)%b
    print(x, end='')