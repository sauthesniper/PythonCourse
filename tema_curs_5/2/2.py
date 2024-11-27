t=open("./tema_curs_5/in.txt")
line=t.readline()
listOfSets=[]
# answerSet=set()
answerSet=set([x for x in line.replace("\n","").split(" ") ])
while line!="":
    currentSet=set([x for x in line.replace("\n","").split(" ") ])
    # print(currentSet)
    # listOfSets.append(currentSet)
    answerSet=currentSet&answerSet
    line=t.readline()
print(answerSet)