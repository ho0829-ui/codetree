n = int(input())
cnt_cr = 0
cnt_hw = 0
cnt_br = 0

for i in range(1,n+1):
    if i % 12 == 0:
        cnt_br += 1
    elif i % 3 == 0:
        cnt_hw += 1
    elif i % 2 == 0:
        cnt_cr += 1
    
print(cnt_cr, cnt_hw, cnt_br)