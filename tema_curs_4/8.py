data=input("String: ").replace(',','').replace('.','').split()
word=input("Word:  ")
data.append(word)
dataDict={}
for key in data:
    if key in dataDict.keys():
        for letter in key:
            if letter in dataDict[key].keys():
                dataDict[key][letter]+=1
            else:
                dataDict[key][letter]=1
    else:
        dataDict[key]={}
        for letter in key:
            if letter in dataDict[key].keys():
                dataDict[key][letter]+=1
            else:
                dataDict[key][letter]=1
ref={}
for letter in word:
    if letter in ref.keys():
        ref[letter]+=1
    else:
        ref[letter]=1
        
for key in dataDict.keys():
    # print(len(dataDict[key].keys()))
    # print(dataDict[key])
    # print(len(ref.keys()))
    # print(key)
    if (len(dataDict[key].keys())==len(ref.keys())):
        for letter in key:
            if letter not in ref.keys():
                break
        else:
            print(key)