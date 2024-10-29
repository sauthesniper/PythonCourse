data=input("STRING: ")
mistake=input("TO REPLACE: ")
correct=input("WITH: ")
wordArray=data.split(" ");
for index in range(len(wordArray)):
    if wordArray[index] == mistake:
        wordArray[index]=correct
    else:
        pass
finalString=" ".join(wordArray);
print(finalString)
