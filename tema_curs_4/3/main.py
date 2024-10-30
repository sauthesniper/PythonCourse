import os
INPUTLOCATION=__file__[0:-7]+'input.txt'
OUTPUTLOCATION=__file__[0:-7]+'output.txt'
input=open(INPUTLOCATION,'r')
output=open(OUTPUTLOCATION,'w')
content=input.read().split(' ')
filteredContent=[]
filteredPair={
    'quantity': 0,
    'price': 0,
    'value': 0,
}
sums=[]
for index in range(len(content)):
    if (content[index].isalpha()):
        continue
    else:
        # continutul nu e strict litere
        content[index]=content[index].split('.')
        number=0
        if (len(content[index])==2):
            if (content[index][0].isnumeric() and content[index][1].isnumeric()):
                number=float(str(content[index][0]) +'.'+ str(content[index][1]))
        elif (content[index][0].isnumeric()):
            number=int(content[index][0])
        else:
            # print('not a number')
            continue;
        if (number!=0):
            # print(number)
            # print(content[index+1])
            if (content[index+1]=="RON"):
                filteredPair["price"]=number
            else:
                filteredPair["quantity"]=number
            if (filteredPair["price"]!=0 and filteredPair["quantity"]!=0):
                filteredPair["value"]=round(filteredPair["quantity"]*filteredPair["price"],2 );
                # print(filteredPair.copy)
                filteredContent.append(filteredPair)
                filteredPair={
                    'quantity': 0,
                    'price': 0,
                    'value': 0,
                }
finalResult=sum(item['value'] for item in filteredContent)
print(finalResult);
