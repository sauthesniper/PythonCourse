data=list();
line=input("String: ");
print(line);
increment=1
# a)
while line!="-1":
    punctaj=line.split(" ")[0];
    nume=line[len(punctaj)+1:len(line)]
    data.append((punctaj,nume,increment))
    increment+=1
    line=input("String: ");
    # print(line);
# print(data)
# b)
punctaje=set()
for part in data:
    punctaje.add(part[0])
print(punctaje)
# c)
scoreDict=dict()
for punctaj in punctaje:
    scoreDict[punctaj]=[x for x in data if x[0]==punctaj]
print(scoreDict)
for punctaj in scoreDict.keys()