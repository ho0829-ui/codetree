lst = [int(input()) for _ in range(5)]
cnt = 0

for i in range(5):
    if lst[i] % 2 == 0:
        cnt += 1

print(cnt)