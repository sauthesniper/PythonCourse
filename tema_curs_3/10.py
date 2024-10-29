data=input("String: ").split(" ")
for part in data:
    if (part.replace('-','').isalpha() and part.count('-')<2 and len(part)>2 and part[0].isupper() and len(part.split('-'))<3):
        continue
    else:
        print('invalid');
        break
else:
    print('valid');
# a very long if