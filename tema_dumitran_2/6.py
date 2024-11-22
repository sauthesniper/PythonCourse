list=[[1,2,3],[3,4,5],[4,5,6],[6,7,8]]
tupl=(1,2,3,-1,2,3,-1,-23,-1,90)
lamTupl= lambda x: x>0
str="Calul meu are o coada, iar coada lui este: foarte mare, foarte groasa, foarte... !"
lamStr= lambda x: x in ".,!:"
anag="adaco coada iar coada daaoc este: foarte coada, adaco groasa, ada... !"
numere=[123,222,333,444,555,123,99,558,882,990]
def anagrama(test,source):
    # test if it's anagram of source
    if sorted(test) !=sorted(source):
        return False
    return True

lamAnag= lambda x: anagrama('coada',x)
lamSumCif= lambda x: 

lam= lambda x: sum(x)>10
lam2= lambda x: 4 in x

def functieGenerica(iterable,criteria):
    tempIterable=[]
    for i in range(len(iterable)):
        print(iterable[i])
        if criteria(iterable[i]):
            tempIterable.append(i)
    return tempIterable
# print(functieGenerica(list,lam2))
# print(functieGenerica(tupl,lamTupl))
# print(functieGenerica(str,lamStr))
print(functieGenerica(anag.split(' '),lamAnag))