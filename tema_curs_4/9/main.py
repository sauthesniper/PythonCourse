import os
inFileName=input("Fisier:")
INPUTLOCATION=__file__[0:-7]+inFileName+'.txt'
OUTPUTLOCATION=__file__[0:-7]+'rime.txt'
input=open(INPUTLOCATION,'r')
output=open(OUTPUTLOCATION,'w')
content=input.read().replace('.','').replace(',','').replace('?','').replace('!','').upper().split()
# print(sorted(content))
for index in range(len(content)):
    buffer=''
    for coindex in range(index,len(content)):
        for rhimeScore in range( min(len(content[coindex]),len(content[index])) ):
            if (content[index]!=content[coindex]):
                if content[index].endswith(content[coindex][ len(content[coindex])- rhimeScore : len(content[coindex])]):
                    continue
                else:
                    if (rhimeScore>2):
                        # print('Rhyme score: '+str(rhimeScore)+' word '+content[index]+' : '+content[coindex])
                        buffer+=content[coindex]+' '
                    break
    if buffer:
        output.write(buffer+(content[index]) )
        output.write('\n')