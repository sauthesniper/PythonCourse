import os
import copy
INPUTLOCATION=__file__[0:-7]+'inventar.txt'
# OUTPUTLOCATION=__file__[0:-7]+'rime.txt'
# input=open(INPUTLOCATION,'r')
# output=open(OUTPUTLOCATION,'w')
# a)
data=dict()
with open(INPUTLOCATION,'r') as file:
    currentLine=file.readline().strip().split();
    while currentLine:
        storeName=currentLine[0]
        currentLine.pop(0)
        currentLine=set(currentLine)
        data[storeName]=currentLine
        currentLine=file.readline().strip().split();
# print(data);
# b)
# we take for reference the first set
intersection=set()
storeNames=list(data.keys());
reference=data[storeNames[0]].copy()
for item in reference:
    for store in storeNames[1:len(storeNames)]:
        if (item in data[store]):
            continue
        else:
            break
    else:
        intersection.add(item)
# print(intersection)
# c)
reunion=set()
for store in storeNames:
    for item in data[store]:
        reunion.add(item)
# print(reunion)
# d)
exclusive=copy.deepcopy(data)
for store in storeNames:
    for item in data[store]:
        for iterationStore in storeNames:
            if item in exclusive[iterationStore] and store != iterationStore:
                exclusive[iterationStore].remove(item)
# print(exclusive)
        