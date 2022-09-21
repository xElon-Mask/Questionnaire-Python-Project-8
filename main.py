"""
1 - Ecrire la question :
2 - Proposez 4 réponses : a, b, c, d avec toujours une seule réponse valide
3 - Demander à l'utilisateur de donner sa réponse.
4 - En fonction de sa réponse, afficher Bonne réponse / Mauvaise réponse
5 - Ensuite, on passe à la 2eme question : Quelle est la capitale de l'Italie ?
6 - et une troisième, et une quatrième
"""

# poser_question(question, r1, r2, r3, r4, choix_bonne_reponse)
def poser_question(pays, r1, r2, r3, r4, bonne_reponse):
    print("Question : Quelle est la capitale de", pays, "?")
    print("a -", r1)
    print("b -", r2)
    print("c -", r3)
    print("d -", r4)
    rep_user = input("Votre réponse :")

    if bonne_reponse == rep_user:
        print("Bonne réponse !")
    else:
        print("Mauvaise réponse.")
    print()


poser_question("France", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Italie", "Rome", "Florence", "Naples", "Vérone", "a")
poser_question("Portugal", "Sintra", "Evora", "Lagos", "Lisbonne", "d")
poser_question("Suisse", "Genève", "Berne", "Lausanne", "Zurich", "b")