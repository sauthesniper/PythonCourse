import sys
sys.setrecursionlimit(1000000)
data=input("Data: ").split(" ")
ziua=data[0]
luna=data[1]
anul=data[2]
ziuaInSaptamana=7

# functions
def incrementZiuaInSaptamana():
    global ziuaInSaptamana
    ziuaInSaptamana=(ziuaInSaptamana+1)%7 +1
def printZiuaInSaptamana():
    global ziuaInSaptamana
    saptamanaDict={
        1: "luni",
        2: "marti",
        3: "miercuri",
        4: "joi",
        5: "vineri",
        6: "sambata",
        7: "duminica",
    }
    print(saptamanaDict[ziuaInSaptamana])
def alphaMonthToIntMonth(monthName):
    lunaDict={
        "ianuarie": 1,
        "februarie": 2,
        "martie": 3,
        "aprilie": 4,
        "mai": 5,
        "iunie": 6,
        "iulie": 7,
        "august": 8,
        "septembrie": 9,
        "octombrie": 10,
        "noiembrie": 11,
        "decembrie": 12,
    }
    return lunaDict[monthName]
def daysPerMonth(monthID,year):
    if (monthID!=2):
        dict={
            1:31,
            2:"februarie",
            3:31,
            4:30,
            5:31,
            6:30,
            7:31,
            8:31,
            9:30,
            10:31,
            11:30,
            12:31,
        }
        return dict[monthID]
    else:
        if (year%4!=0):
            # common year
            return 28
        elif (year%100!=0):
            # leap year 
            return 29
        elif (year%400!=0):
            # common year
            return 28
        else :
            return 29
        
def RECINCR(ziua,luna,anul, Fziua,Fluna,Fanul ):
    if (ziua==Fziua and luna==Fluna and anul == Fanul):
        print("finished")
        printZiuaInSaptamana()
        return
    maxZiua=daysPerMonth(luna,anul)
    maxLuna=12
    if (ziua<maxZiua):
        ziua+=1
        incrementZiuaInSaptamana()
    else:
        ziua=1
        incrementZiuaInSaptamana()
        if luna<maxLuna:
            luna+=1
        else:
            luna=1
            anul+=1
    print(ziua,luna,anul," ")
    if (anul<Fanul+1):
        RECINCR(ziua,luna,anul,Fziua,Fluna,Fanul)
# main
ziua=int(ziua)
luna=int(luna)
amnul=int(anul)
RECINCR(1,1,2024,ziua,luna,anul)
