"""
1 - Ecrire la question :
2 - Proposez 4 réponses : a, b, c, d avec toujours une seule réponse valide
3 - Demander à l'utilisateur de donner sa réponse.
4 - En fonction de sa réponse, afficher Bonne réponse / Mauvaise réponse
5 - Ensuite, on passe à la 2eme question : Quelle est la capitale de l'Italie ?
6 - et une troisième, et une quatrième
"""
def demander_reponse_numerique_utilisateur(min, max):
    rep_user_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + "):")
    try:
        rep_user_int = int(rep_user_str)
        if min <= rep_user_int <= max:
            return rep_user_int

        print("ERREUR: Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR: Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(min, max)
    


# poser_question(titre_question, r1, r2, r3, r4, choix_bonne_reponse)
def poser_question(question):
    print("QUESTION")
    print(" " + question[0])
    for rep_pos in range(len(question[1])):
        print(rep_pos +1, "-", question[1][rep_pos])
   
    print()
    resultat_response_correcte = False
    rep_user_int = demander_reponse_numerique_utilisateur(1, len(question[1]))
    if question[1][rep_user_int-1] == question[2]:
        print("Bonne réponse !")
        resultat_response_correcte = True
    else:
        print("Mauvaise réponse.")

    print()
    return resultat_response_correcte



def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
        # sous entendu if poser_question(question) == True:
            score += 1
    print("Score final :", score, "sur", len(questionnaire))


questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Florence", "Naples", "Vérone"), "Rome" ),
    ("Quelle est la capitale du Portugal ?", ("Sintra", "Evora", "Lagos", "Lisbonne"), "Lisbonne"),
    ("Quelle est la capitale de la Suisse ?", ("Genève", "Berne", "Lausanne", "Zurich"), "Berne")
                )


lancer_questionnaire(questionnaire)

