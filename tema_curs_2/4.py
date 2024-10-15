# care este cauza pentru x-1?
# simplu, calculam care este gradul celui mai semnificativ bit din reprezentarea binara
x=129
x=x-1
cnt=0
while x:
    cnt=cnt+1
    x=x>>1
print(f"Raspuns: {2**cnt}")