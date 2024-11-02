import os
INPUTLOCATION=__file__[0:-7]+'in.tst'
input=open(INPUTLOCATION,'r')
finDict=[]
with open(INPUTLOCATION,'r') as file:
    while 1:
        line=file.readline();
        if (line):
            person={
                "nume" : "",
                "prenume" : "",
                "adresa" : {
                    "strada": "",
                    "numar": "",
                    "oras": ""
                }
            }
            beginAd=line.find('adresa')
            for data in line[0:beginAd].replace('\n','').split(','):
                temp=data.split(':')
                if (len(temp)>1):
                    person[temp[0]]=temp[1].strip()
            for addressData in line[beginAd+7:len(line)].replace('\n','').replace('}','').replace('{','').split(','):
                temp=addressData.split(':')
                if (len(temp)>1):
                    person["adresa"][temp[0]]=temp[1].strip()
            print(person);
            finDict.append(person)
        else:
            break
dict2=[x for x in finDict if x["adresa"]["oras"]=="Bucuresti" ]
print(dict2)