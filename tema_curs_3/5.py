inputData=input("Input: ")
key=input("Key: ")
task=input("encrypt (1), decrypt: (0): \n")
task=int(task)
key=int(key)
if (task):
    print('encrypting...')
    cipher=[]
    for char in inputData:
        print(ord(char))
        cipher.append( chr( (ord(char) + key )))
    cipher="".join(cipher);
    print("Cipher text: "+cipher);
else:
    print("decrypting...")
    cipher=inputData;
    plain=[]
    for char in cipher:
        plain.append( chr( (ord(char) - key ) ))
    plain="".join(plain);
    print("Plain text: "+plain)


# face ceea ce trebuie decat ca nu face operatia modulo, ca N-ARE SENS!