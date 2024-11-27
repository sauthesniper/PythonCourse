n=int(input("N:"))
m=[]
for i in range(n):
    m.append(int(input()))
# m=[int(x) for x in (input().split(" "))]
currentBigs=[0,0]
currentSmalls=[0,0]
if (m[0]<m[1]):
    currentBigs=[m[0],[1]]
else:
    currentBigs=[m[1],[0]]
def updateBig(a):
    if a>currentBigs[0]:
        currentBigs[1]=currentBigs[0]
        currentBigs[0]=a
    elif a>currentBigs[1]:
        currentBigs[1]=a
def updateSmall(b):
    if (b<currentSmalls[0] & b>currentSmalls[1]):
        currentSmalls[0]=b
    elif (b<currentSmalls[1]):
        currentSmalls[0]=currentSmalls[1]
        currentSmalls[1]=b
for num in m:
    updateBig(num)
    updateSmall(num)
print(currentBigs)
print(currentSmalls)
if (currentBigs[0]*currentBigs[1]>currentSmalls[0]*currentSmalls[1]):
    print(currentBigs[0]*currentBigs[1])
else:
    print(currentSmalls[0]*currentSmalls[1])
