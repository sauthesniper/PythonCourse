import random
file=open('tema_curs_4\\1\\input.txt','r')
out=open('tema_curs_4\\1\\output.txt','w')
for nume in file.readlines():
    email=nume.replace(' ','.').lower().strip()+'@myfmi.unibuc.ro'
    parola= ''.join([chr(random.randint(60,90)) for x in range(4)])+str(random.randint(1000,9999))
    out.write(email+','+parola+'\n');