# Lista de studenți
studenti = [
    {"nume": "Ana Popescu", "grupa": "101", "credite": [5, 7, 8, 9, 10]},
    {"nume": "Mihai Ionescu", "grupa": "102", "credite": [6, 8, 9, 7, 6]},
    {"nume": "Elena Vasilescu", "grupa": "103", "credite": [10, 9, 9, 8, 10]},
    {"nume": "Radu Georgescu", "grupa": "104", "credite": [7, 7, 6, 8, 9]},
    {"nume": "Ioana Dumitru", "grupa": "105", "credite": [9, 9, 10, 10, 10]},
    {"nume": "Vlad Popa", "grupa": "106", "credite": [6, 7, 8, 6, 7]},
    {"nume": "Cristina Marin", "grupa": "107", "credite": [8, 9, 10, 9, 10]},
    {"nume": "Andrei Dobre", "grupa": "103", "credite": [7, 7, 8, 7, 8]},
    {"nume": "Maria Petrescu", "grupa": "109", "credite": [9, 9, 10, 10, 10]},
    {"nume": "Alexandru Rusu", "grupa": "101", "credite": [6, 6, 7, 8, 9]},
    {"nume": "Daniela Pavel", "grupa": "101", "credite": [10, 10, 10, 10, 10]},
    {"nume": "Ion Barbu", "grupa": "112", "credite": [5, 6, 7, 8, 9]},
    {"nume": "Gabriela Neagu", "grupa": "101", "credite": [8, 9, 8, 9, 10]},
    {"nume": "Florin Munteanu", "grupa": "104", "credite": [7, 7, 8, 8, 9]},
    {"nume": "Raluca Zadea", "grupa": "105", "credite": [10, 9, 9, 10, 10]},
    {"nume": "Raluca Badea", "grupa": "105", "credite": [10, 9, 9, 10, 10]},
]

for student in studenti:
    student["promovat"]= 0 not in student["credite"] and sum(student["credite"])>35
# crescator dupa grupa si in fiecare grupa in ordine alfabetica:
studenti=sorted(studenti,key= lambda stud: stud["grupa"]+' '+stud["nume"])
# intai cei promovati apoi cei nepromovati si in ordine alfabetica
studenti=sorted(studenti,key=lambda stud: (not stud["promovat"], stud["nume"]))
# descrescator dupa suma creditelor, crescator dupa grupa si alfabetic dupa nume
studenti=sorted(studenti,key= lambda stud: (-sum(stud["credite"]), stud["grupa"], stud["nume"]))
# crescator dupa grupa, descrescator dupa promovabilitate,descrescator dupa suma creditelor, alfabetic dupa nume
studenti=sorted(studenti,key=lambda s: (s["grupa"], not s["promovat"], -sum(s["credite"]), s["nume"]))
for student in studenti:
    print(student)