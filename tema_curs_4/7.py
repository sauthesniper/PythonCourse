dict1={
    "t": 2,
    "s": 14,
    "a":201
}
dict2={
    "b": 2,
    "s": 14,
    "a":201
}
for a in dict2.keys():
    if a in dict1.keys():
        dict1[a]+=dict2[a]
    else:
        dict1[a]=dict2[a]
for a in dict1.keys():
    print(a,dict1[a],sep=':',end='\n')