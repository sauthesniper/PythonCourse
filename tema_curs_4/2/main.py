input=open('./tema_curs_4/1/input.txt')
output=open('./tema_curs_4/1/output.txt','w')
score=0
for line in input.readlines():
    line=line.strip()
    content=line.split("*");
    content=[content[0]] +list(content[1].split('='))
    for index in range(3):
        content[index]=int(content[index])
    if (content[0]*content[1]==content[2]):
        line+=' Corect'
        score+=1
    else:
        line+=' Gresit '+ str(content[0]*content[1])
    output.write(line+'\n');
output.write("Nota: "+str(score+1))
