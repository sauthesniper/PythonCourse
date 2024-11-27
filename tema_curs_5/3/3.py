t=open("./tema_curs_5/in.txt")
content=t.read().replace('\n',' ').replace(',','').replace('.','').replace('!','').lower().split(' ')
multimi=dict()
# multimi=set([  for word in content])
def obtainKey(word):
    key=[];
    keySet=set();
    word=sorted(word)
    for letter in word:
        if letter not in keySet:
            key.append(letter)
        keySet.add(letter)
    key="".join(key)
    return key
for word in content:
    # key="".join())
    key=obtainKey(word)
    if key in multimi.keys():
        multimi[key].add(word)
    else:
        multimi[key]={word}
sortedKeys=sorted(multimi.keys(),key=lambda x: (-len(x),x) )
print(sortedKeys);
# print(multimi);
for key in sortedKeys:
    print("Literele "+key+': ',end=' ')
    for word in multimi[key]:
        print(word,end=' ')
    print()
multimi.keys()