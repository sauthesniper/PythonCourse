#solutia consta in crearea unei variabila de suma careia i se urmareste maximul
# incrementarea sumei se face cand ultimul bit al unei shiftari este 1
maxl=0
curl=0
num=255

while num :
    if (num & 1):
        curl=curl+1
    else : 
        curl=0
    if maxl < curl :
        maxl=curl 
    num=num>>1

print(f"Lungimea maxima este {maxl} biti 1 consecutivi")
