def genXinList(x,listArray):
    while (len(listArray)!=0):
        if x in listArray[0]:
            yield listArray[0]
            listArray.pop(0)
        else:
            listArray.pop(0)
data=[[1,2,3],[3,4,5],[4,5,6],[5,6,7]]
for i in genXinList(5,data):
    print(i)