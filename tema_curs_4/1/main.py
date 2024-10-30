data=input("Input text: ").split()
freqData={}
for word in data:
    if (word in freqData.keys()):
        freqData[word]+=1
    else:
        freqData[word]=1
print( list(sorted(freqData.items(), key=lambda item: (10-item[1],item[0]) ,reverse=False)) )
print( list(sorted(freqData.items(), key=lambda item: [item[1],item[0]] ,reverse=True)) )
# print( dict(sorted(freqData.items(), key=lambda item: str(item[1])+str(item[0]) ,reverse=False)));