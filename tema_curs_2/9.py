data=input("String: ")
stri=0
values=[]
endi=len(data)
while stri<endi:
    location=data.find('$',stri+1)
    if (location!=-1):
        stri=location
        # print(location)
        # print(data[location+1:endi])
        number=''
        for letter in data[location+1:endi]:
            if str(letter).isnumeric():
                number=number+str(letter)
            else:
                break
        print(number)
        values.append(number);
    else:
        print("FINAL")
        break;
# a)
print(values[0]," , ",values[1])
print(values[len(values)-2]," , ",values[len(values)-1]);
if (values[len(values)-1]==values[len(values)-2]):
    print('s-au inteles')
else:
    print('nu s-au inteles')