list=[[1,2,3],[3,4,5],[4,5,6],[6,7,8]]
lam= lambda x: sum(x)>10
lam2= lambda x: 4 in x
print(lam(list[0]))
def functieGenerica(iterable,criteria):
    tempIterable=[]
    for i in range(len(iterable)):
        if criteria(iterable[i]):
            tempIterable.append(i)
    return tempIterable
print(functieGenerica(list,lam2))