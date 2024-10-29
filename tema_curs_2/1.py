data=input("String : ")
gresit=input("Mistake : ")
correct=input("Replace : ")
data=str(data)
data=data.replace(gresit,correct);

answerString="Propozitia corecta este :\n {propozitie}"
answerString=answerString.format(propozitie=data)
print(answerString);