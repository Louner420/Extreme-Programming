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
    try:
        anzahl = int(input("Wie viele Fragen: "))

    except ValueError:
        print("Gib mir eine Anzahl")

def getKategorie():
    global kategorie
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

    except ValueError:
        print("Gib mir eine Kategorie")

def getDifficulty():
    global schwierigkeit
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

    except ValueError:
        print("Gib mir eine Schwierigkeit")

def getType():
    global typ
    try:
        print("Typ:\n"
              "1: Multiple Choice\n"
              "2: Wahr/Falsch\n")

        typ = int(input("Welchen Typ: "))

        match typ:
            case 1:
                typ = "multiple"
            case 2:
                typ = "boolean"
            case _:
                print("Das steht leider nicht zu Auswahl")

    except ValueError:
        print("Gib mir einen Typ")

def getQuestions():
    global Highscore
    score = 0
    api_url = f"https://opentdb.com/api.php?amount={anzahl}&category={kategorie}&difficulty={schwierigkeit}&type={typ}"
    response = req.get(api_url)
    if response.status_code == 200:

        data = response.json()
        for i in range(anzahl):
            for j in range(3):
                Antworten.append(data['results'][i]['incorrect_answers'][j])
            Antworten.append(data['results'][i]['correct_answer'])
            rand.shuffle(Antworten)
            print(f"Frage {i+1}: {data['results'][i]['question']}")
            print(f"Antwortmöglichkeiten: {Antworten}")
            try:
                antwort = input("Antwort: ")
                if antwort == data['results'][i]['correct_answer']:
                    print("Korrekt")
                    score += 1
                    Antworten.clear()

                else:
                    print("Falsch")
                    score = 0
                    Antworten.clear()
            except ValueError:
                print("Gib mir eine Antwort")

            if score > Highscore:
                Highscore = score

            print(f"Korrekte Antwort: {data['results'][i]['correct_answer']}")
            #print(f"Falsche Antworten: {data['results'][i]['incorrect_answers']}")
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

quizMaster()