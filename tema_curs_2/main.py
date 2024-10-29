# tratand cazul in care avem numarul N 
# vom face XOR intre toate elementele array-ului ->b
# vom face XOR intre toate numerele range(1,n) ->a
# a^b = x^y, determinam bruteforce care sunt x si y, intrucat daca x=6 atunci y=a^b^6.
n=10
arr=[1,2,3,4,5,8,9]
arrXOR=0
totalXOR=0
for i in range(0,n):
    totalXOR=totalXOR^i
    if i<len(arr):
        arrXOR=arrXOR^arr[i]
FXOR=totalXOR^arrXOR
for test in range(1,n):
    intA=test
    intB=FXOR^test
    if intA not in arr:
        print(f"Numerele lipsa sunt {intA} si {intB}")
        break