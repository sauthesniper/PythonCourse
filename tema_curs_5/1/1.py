t=open("./tema_curs_5/in.txt").readline().split(" ");
xorSet=0
xorN=0
for x in range(len(t)):
    xorSet=xorSet^int(t[x])
    print(int(t[x]), end=' ');
print()
for x in range(1,len(t)+2):
    xorN=xorN^x
    print(x, end=' ');
print()
print(xorN^xorSet)
exit()

# sau
t=open("./tema_curs_5/in.txt").readline().split(" ");
setA=set([int(x) for x in range(1,len(t)+2)]);
setB=set(int(x) for x in t  );
print(setA);
print(setB);
ans=setA-setB;
print(ans);