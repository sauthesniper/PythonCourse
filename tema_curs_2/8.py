# a)
# data=input("String: ")
# data=data.replace('e','epe')
# data=data.replace('a','apa')
# data=data.replace('i','ipi')
# data=data.replace('o','opo')
# data=data.replace('u','upu')
# print("String: " + data)
# b)

data=input("String: ")
def do():
    global data
    data=data.replace('e','epe')
    data=data.replace('E','Epe')
    data=data.replace('a','apa')
    data=data.replace('A','Apa')
    data=data.replace('i','ipi')
    data=data.replace('I','Ipi')
    data=data.replace('o','opo')
    data=data.replace('O','Opo')
    data=data.replace('u','upu')
    data=data.replace('U','Upu')
def undo():
    global data
    data=data.replace('epe','e')
    data=data.replace('Epe','E')
    data=data.replace('apa','a')
    data=data.replace('Apa','A')
    data=data.replace('ipi','i')
    data=data.replace('Ipi','I')
    data=data.replace('opo','o')
    data=data.replace('Opo','O')
    data=data.replace('upu','u')
    data=data.replace('Upu','U')
do()
print("String: " + data)
undo()
print("String: " + data)

data=data.replace('-','')
print("String2: " + data)

# b) da, aparent merge si se face asa.
# exista metode mai optime,dar asta e ceva functional