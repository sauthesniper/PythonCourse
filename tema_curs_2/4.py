data1=input("STRING 1:")
data2=input("STRING 2:")
if (len(data1)>len(data2)):
    data1, data2= data2, data1

for i in range(len(data2)):
    count1=data1.count(data1[i])
    count2=data2.count(data2[i])
    if count1!=count2:
        print('anagrame')
        break
else:
    print("neanagrame")