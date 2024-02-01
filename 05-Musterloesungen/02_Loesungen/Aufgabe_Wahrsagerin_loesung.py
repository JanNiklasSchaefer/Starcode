import random

def wahrsagerin():
    
    antworten = [
        "Es ist sicher.",
        "Es steht außer Frage.",
        "Ohne Zweifel.",
        "Ja, definitiv.",
        "Du kannst dich darauf verlassen.",
        "Wie ich es sehe, ja.",
        "Sehr wahrscheinlich.",
        "Aussicht gut.",
        "Ja.",
        "Die Zeichen deuten auf Ja.",
        "Antwort unklar, versuche es erneut.",
        "Frage später noch einmal.",
        "Besser, ich sage es dir jetzt nicht.",
        "Kann ich jetzt nicht vorhersagen.",
        "Zweifelhaft.",
        "Meine Quellen sagen nein.",
        "Aussichten nicht so gut.",
        "Sehr fraglich."
    ]

    
    frage = input("Stelle der Wahrsagerin eine Ja- oder Nein-Frage: ")

    
    antwort = random.choice(antworten)

    
    print("Die Wahrsagerin sagt:", antwort)


wahrsagerin()

