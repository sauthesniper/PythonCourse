data = {}
n = int(input("Persoane "))
q = int(input("Intrebari "))

for i in range(n):
    name = input("Nume ")
    age = int(input("Varsta "))
    if age in data:
        data[age].add(name)
    else:
        data[age] = {name}

for i in range(q):
    id = int(input())
    if id in data:
        print(" si ".join(data[id]))
    else:
        print("No data found for ID:", id)