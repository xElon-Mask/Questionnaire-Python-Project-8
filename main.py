"""
1 - Ecrire la question :
2 - Proposez 4 réponses : a, b, c, d avec toujours une seule réponse valide
3 - Demander à l'utilisateur de donner sa réponse.
4 - En fonction de sa réponse, afficher Bonne réponse / Mauvaise réponse
5 - Ensuite, on passe à la 2eme question : Quelle est la capitale de l'Italie ?
6 - et une troisième, et une quatrième
"""

# poser_question(titre_question, r1, r2, r3, r4, choix_bonne_reponse)
def poser_question(question):
    global score
    print("QUESTION")
    print(" " + question[0])
    for rep_pos in question[1]:
        print(rep_pos)
    # print(question[1][0])
    # print(question[1][1])
    # print(question[1][2])
    # print(question[1][3])
    rep_user = input("Votre réponse :")

    if question[2].lower() == rep_user:
        print("Bonne réponse !")
        score += 1
    else:
        print("Mauvaise réponse.")
    print()

score = 0


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Florence", "Naples", "Vérone"), "Rome" )

poser_question(question1)
poser_question(question2)
#poser_question("Portugal", "Sintra", "Evora", "Lagos", "Lisbonne", "d")
#poser_question("Suisse", "Genève", "Berne", "Lausanne", "Zurich", "b")

print("Score final :", score)