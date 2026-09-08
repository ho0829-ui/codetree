lst = [int(input()) for _ in range(10)]
cnt = 0

for i in range(10):
    if lst[i]%2==1:
        cnt += 1

print(cnt)