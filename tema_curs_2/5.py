# sa mai zic?

x=600
cnt=0
while x:
    cnt = cnt + int(not(x&1))
    x=x>>1
print(cnt)