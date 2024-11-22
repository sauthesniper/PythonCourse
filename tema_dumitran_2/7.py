carti=[
    {
        "titlu": "Sapiens: A Brief History of Humankind",
        "autor": "Yuval Noah Harari",
        "an_aparitie": 2011,
        "pret": 50.00
    },
    {
        "titlu": "1984",
        "autor": "George Orwell, George Orwell, George Orwell",
        "an_aparitie": 1949,
        "pret": 30.00
    },
    {
        "titlu": "To Kill a Mockingbird",
        "autor": "Harper Lee, Harper Lee",
        "an_aparitie": 1960,
        "pret": 35.00
    },
    {
        "titlu": "Pride and Prejudice",
        "autor": "Jane Austen",
        "an_aparitie": 1813,
        "pret": 25.00
    },
    {
        "titlu": "The Great Gatsby",
        "autor": "F. Scott Fitzgerald",
        "an_aparitie": 1925,
        "pret": 40.00
    },
    {
        "titlu": "Moby Dick",
        "autor": "Herman Melville",
        "an_aparitie": 1851,
        "pret": 45.00
    },
    {
        "titlu": "War and Peace",
        "autor": "Leo Tolstoy,Leo Tolstoy ,Leo Tolstoy",
        "an_aparitie": 1869,
        "pret": 55.00
    },
    {
        "titlu": "The Catcher in the Rye",
        "autor": "J.D. Salinger",
        "an_aparitie": 1951,
        "pret": 28.00
    },
    {
        "titlu": "Brave New World",
        "autor": "Aldous Huxley",
        "an_aparitie": 1932,
        "pret": 32.00
    },
    {
        "titlu": "Crime and Punishment",
        "autor": "Fyodor Dostoevsky",
        "an_aparitie": 1866,
        "pret": 60.00
    },
    {
        "titlu": "Jane Eyre",
        "autor": "Charlotte Brontë",
        "an_aparitie": 1847,
        "pret": 42.00
    },
    {
        "titlu": "The Hobbit",
        "autor": "J.R.R. Tolkien",
        "an_aparitie": 1937,
        "pret": 50.00
    },
    {
        "titlu": "The Divine Comedy",
        "autor": "Dante Alighieri",
        "an_aparitie": 1320,
        "pret": 70.00
    },
    {
        "titlu": "One Hundred Years of Solitude",
        "autor": "Gabriel García Márquez",
        "an_aparitie": 1967,
        "pret": 48.00
    },
    {
        "titlu": "The Brothers Karamazov",
        "autor": "Fyodor Dostoevsky",
        "an_aparitie": 1880,
        "pret": 65.00
    },
    {
        "titlu": "Wuthering Heights",
        "autor": "Emily Brontë",
        "an_aparitie": 1847,
        "pret": 38.00
    },
    {
        "titlu": "The Alchemist",
        "autor": "Paulo Coelho",
        "an_aparitie": 1988,
        "pret": 32.00
    },
    {
        "titlu": "Anna Karenina",
        "autor": "Leo Tolstoy",
        "an_aparitie": 1877,
        "pret": 58.00
    },
    {
        "titlu": "Harry Potter and the Sorcerer's Stone",
        "autor": "J.K. Rowling",
        "an_aparitie": 1997,
        "pret": 45.00
    },
    {
        "titlu": "The Odyssey",
        "autor": "Homer",
        "an_aparitie": -800,
        "pret": 30.00
    }
]

def ieftinire(array):
    for carte in array:
        if (carte["an_aparitie"]<2000):
            carte["pret"]*=0.8
            carte["pret"]=round(carte["pret"],2)
    return 
def lA():
    return sorted(carti, key = lambda x : (-x["an_aparitie"],x["titlu"] ))
def lB():
    return sorted(carti,key = lambda x : ( len(x.split(',')), -x["pret"] ))
def lC():
    return sorted(carti,key = lambda x : ( x.split(' ')[1] , x.split(' ')[0], x["titlu"], x["an_aparitie"] ))
# print(ieftinire(carti))
# print(lA())
# print(lB())
# print(lC())