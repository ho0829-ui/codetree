a, b, c = map(int, input().split())
max_n = a
for i in (a,b,c):
    if max_n <= i:
        max_n = i
print(max_n)