data=input("Propozitie: ").split(' ')
sum=0
for word in data:
    if(word.isnumeric()):
        sum+=int(word)
print("Suma cheltuita de ANA este : "+str(sum))