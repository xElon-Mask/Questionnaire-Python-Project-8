# PROJET QUESTIONNAIRE V3 : POO
# 
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement

# => Définir les entités (données, actions)
# Ecrire peut être cette classe là ; elle possédera ces champs là, ces différentes méthodes, etc.
#
# Question
#   - titre             - str
#   - choix             - (str)
#   - bonne_reponse     - str
#
#   - poser()     -> bool (est-elle vraie ou fausse ?)
# 
#   Questionnaire
#    - questions          - (Question)
#    - lancer()

class Question:
    def __init__(self, titre: str, choix: (str), bonne_reponse: str):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def poser(self):
        print("QUESTION")
        print(("  ") + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte


        # rep_user = input(self.titre)
        # if rep_user == self.bonne_reponse:
        #     return True
        # return False

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return demander_reponse_numerique_utlisateur(min, max)
        

'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''
def poser_question(question):
    # titre_question, r1, r2, r3, r4, choix_bonne_reponse
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION")
    print("  " + question[0])
    

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

#lancer_questionnaire(questionnaire)

q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q1.poser()


