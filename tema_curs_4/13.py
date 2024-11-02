n=int(input("the num: "))
mat=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(1+i*n+j)
        print(1+i*n+j,' ',end='')
    mat.append(a);
    print('\n')
# mat2=[ [rw*n+a+1 for a in range(n)] for rw in range(n) ]
# print(mat2)

# left=0
# bottom=1
# right=2
# up=3
# b)
listTuplu=[]
maxCap=int(n-1)
TMAX=n*n
TCUR=0
curCap=0
dir=0
i=0
j=0
while maxCap!=0:
    TCUR+=1
    if (TCUR==TMAX):
        break
    match dir:
        case 0:
            j+=1
        case 1:
            i+=1
        case 2:
            j-=1
        case 3:
            i-=1
    curCap+=1         
    if curCap==maxCap:
        curCap=0
        dir+=1
        dir%=4
        if (dir==0):
            maxCap-=2
            i+=1
            j+=1
    listTuplu.append( (i,j));
print(1);
for t in listTuplu:
    print (mat[t[0]][t[1]],sep=' ')