data=input("String: ");
# print(data)
data=data.split('.');
# print(data);
newData=[]
for prop in data:
    prop=prop.strip()
    if (prop[0].isupper()):
        newData.append(prop)
    else:
        continue;
print();
print();
print();
print();
print('. '.join(newData));