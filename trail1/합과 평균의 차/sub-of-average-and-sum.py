a, b, c = map(int, input().split())
sum_n = a+b+c
avg_n = (a+b+c)//3
print(sum_n, avg_n, sum_n-avg_n, sep='\n')