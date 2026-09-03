A = input().split()
B = input().split()
C = input().split()
for t in (A,B,C):
    t[1] = int(t[1])
cnt = 0

for p in (A, B, C):
    if p[0] == 'Y' and p[1] >= 37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')