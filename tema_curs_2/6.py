# artificii dar nimic nou
n=2
arr=range(1,n)
finalXOR=0
def generate(startNumber=0,current=[]):
    global n
    global arr
    global finalXOR
    if (current):
        for element in current:
            finalXOR=finalXOR^element

    for i in range(startNumber,len(arr)):
        current.append(arr[i])
        generate(i+1,current)
        current.pop()

generate()
print(finalXOR)