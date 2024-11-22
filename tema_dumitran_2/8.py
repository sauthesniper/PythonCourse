siruri_caractere = [
    "python",
    "programare",
    "șir",
    "listă",
    "exemplu",
    "cod",
    "variabilă",
    "funcție",
    "buclă",
    "dicionar",
    "tuplu",
    "set",
    "imprimare",
    "intrare",
    "fișier",
    "modul",
    "clasă",
    "obiect",
    "erorare",
    "teste"
]
n=6
def gen(siruri_caractere,n):
    while(siruri_caractere):
        if (len(siruri_caractere[0])==n):
            siruri_caractere.pop(0)
            return siruri_caractere[0]
        else:
            siruri_caractere.pop(0)

for i in gen(siruri_caractere,6):
    print(i)