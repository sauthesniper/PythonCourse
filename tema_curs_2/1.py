#xor de orice numar par de ori dintr-un numar este 0, xor de n cu 0 este n
# daca facem xor pe toate numerele obtinem solutia
curentXOR=0
arr=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

for a in arr:
    curentXOR=curentXOR^a
print(curentXOR)