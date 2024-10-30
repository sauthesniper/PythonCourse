data=input("Input text: ").split()
data=[int(item) for item in data]
currentMax=data[0]
currentMin=data[0]
def newMax(num):
    global currentMax
    if (num>currentMax):
        currentMax=num
        return 1
    else:
        return 0
def newMin(num):
    global currentMin
    if (num<currentMin):
        currentMin=num
        return 1
    else:
        return 0
currentMax=[num for num in data if newMax(num)][-1]
currentMin=[num for num in data if newMin(num)][-1]
print(currentMax)
print(currentMin)