import requests as req
import json
import random as rand

anzahl = 1
kategorie = 0
schwierigkeit = ""
typ = ""
Antworten=[]

Highscore = 0
def getAmount():
    global anzahl
    while True:
        try:
            anzahl = int(input("Wie viele Fragen: "))
            break
        except ValueError:
            print("Gib mir eine Anzahl")

def getKategorie():
    global kategorie
    while True:
        try:
            print("Kategorien:\n"
                "1: Allgemeinwissen\n"
                "2: Geographie\n"
                "3: Geschichte\n")

            kategorie = int(input("Welche Kategorie willst du: "))

            match kategorie:
                case 1:
                    kategorie = 9
                case 2:
                    kategorie = 22
                case 3:
                    kategorie = 23
                case _:
                    print("Das steht leider nicht zu Auswahl")
            break

        except ValueError:
            print("Gib mir eine Kategorie")

def getDifficulty():
    global schwierigkeit
    while True:
        try:
            print(f"Schwierigkeitsgrad:\n"
                "1: leicht\n" 
                "2: mittel\n"
                "3: schwer\n")

            schwierigkeit = int(input("Welche Schwierigkeit: "))

            match schwierigkeit:
                case 1:
                    schwierigkeit = "easy"
                case 2:
                    schwierigkeit = "medium"
                case 3:
                    schwierigkeit = "hard"
                case _:
                    print("Das steht leider nicht zu Auswahl")
            break

        except ValueError:
            print("Gib mir eine Schwierigkeit")

def getType():
    global typ
    global kategorieint
    while True:
        try:
            print("Typ:\n"
                "1: Multiple Choice\n"
                "2: Wahr/Falsch\n")

            typ = int(input("Welchen Typ: "))

            match typ:
                case 1:
                    typ = "multiple"
                    kategorieint=3
                case 2:
                    typ = "boolean"
                    kategorieint=1
                case _:
                    print("Das steht leider nicht zu Auswahl")
            break

        except ValueError:
            print("Gib mir einen Typ")

def getQuestions():
    global Highscore
    global Antworten
    score = 0
    api_url = f"https://opentdb.com/api.php?amount={anzahl}&category={kategorie}&difficulty={schwierigkeit}&type={typ}"
    response = req.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for i in range(anzahl):
            if kategorieint==3:
                for j in range(3):
                    Antworten.append(data['results'][i]['incorrect_answers'][j])
                Antworten.append(data['results'][i]['correct_answer'])
                rand.shuffle(Antworten)
                print(f"Frage {i+1}: {data['results'][i]['question']}")
                print(f"Antwortmöglichkeiten: 1: {Antworten[0]}, 2: {Antworten[1]}, 3: {Antworten[2]}, 4: {Antworten[3]}")

                antwort = input("Antwort 1-4 geht auch: ")
                try:

                    antwort = int(antwort)
                    while antwort > 4 or antwort < 0:
                        print("falsche Zahl du Fisch!")
                        antwort = input("Antwort 1-4 geht auch: ")
                        antwort = int(antwort)
                    antwort -= 1
                    if Antworten[antwort] == data['results'][i]['correct_answer']:
                        print("Korrekt")
                        score += 1
                    else:
                        print("Falsch")
                        score = 0
                except TypeError:
                    if antwort == data['results'][i]['correct_answer']:
                        print("Korrekt")
                        score += 1
                    else:
                        print("Falsch")
                        score = 0
                Antworten.clear()
                if score > Highscore:
                    Highscore = score

                print(f"Korrekte Antwort: {data['results'][i]['correct_answer']}")
                print(f"derzeitiger score: {score}")
            else:
                Antworten=["True","False"]
                print(f"Frage {i+1}: {data['results'][i]['question']}")
                print(f"Antwortmöglichkeiten: 1: {Antworten[0]}, 2: {Antworten[1]}")
            
                antwort = input("Antwort 1 oder 2 geht auch: ")
                try:
                    antwort = int(antwort)-1
                    if Antworten[antwort] == data['results'][i]['correct_answer']:
                        print("Korrekt")
                        score += 1
                    else:
                        print("Falsch")
                        score = 0
                except TypeError:
                    if antwort == data['results'][i]['correct_answer']:
                        print("Korrekt")
                        score += 1
                    else:
                        print("Falsch")
                        score = 0
                Antworten.clear()
                if score > Highscore:
                    Highscore = score

                
                print(f"Korrekte Antwort: {data['results'][i]['correct_answer']}")
                print(f"derzeitiger score: {score}")
            
    else:
        print("Problem mit der API-Abfrage")

def quizMaster():
    global Highscore
    print("Willkommen beim QuizMaster")
    print(f"Dein Highscore ist: {Highscore}")
    print("1: Neues Quiz starten")
    print("2: Beenden")
    auswahl = input("Was willst du tun: ")

    if auswahl == "1":
        main()
    elif auswahl == "2":
        print("Tschüss")
    else:
        print("Das steht leider nicht zur Auswahl")
        quizMaster()
def main():
    getAmount()
    getKategorie()
    getDifficulty()
    getType()
    getQuestions()

while True:
    quizMaster()