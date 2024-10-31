data=input("String: ")
dict={}
for letter in data:
    if letter in dict.keys():
        dict[letter]+=1
    else:
        dict[letter]=1
for a in dict.keys():
    print(a+' : '+str(dict[a]))