n = int(input())
lst = [int(input()) for _ in range(n)]

for i in range(n):
    if lst[i]%2==1 and lst[i]%3==0:
        print(lst[i])