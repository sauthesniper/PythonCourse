# similar cu #0
x=input("Variabila X: ")
y=input("Variabila Y: ")
x=int(x)^int(y)
sum=0
while x:
    sum=sum + int(x&1)
    x=x>>1
print(f"Raspuns : {sum}");