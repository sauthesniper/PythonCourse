import os
INPUTLOCATION=__file__[0:-7]+'ocr.in'
# OUTPUTLOCATION=__file__[0:-7]+'rime.txt'
# input=open(INPUTLOCATION,'r')
# output=open(OUTPUTLOCATION,'w')
content=open(INPUTLOCATION,'r').read().split('\\n');
answ=[]
for line in content:
    formattedString=line.replace('+','').replace('\n','').replace("\"",'').strip();
    if (formattedString):
        word=formattedString.split(':')[0];
        tildas=formattedString.count('~')
        occurances=formattedString.count(word)
        score=tildas+occurances
        item=(word,score)
        answ.append(item)
print(answ)