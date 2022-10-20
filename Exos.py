# #Exo1
#
# prenom = "Pierre"
# age = 20
# majeur = True
# compte_en_banque = 20135.384
# amis = ['Marie', 'Julien', 'Adrien']
# parents = ('Marc', 'Caroline')
#
# print(prenom)
# print(age)
# print(majeur)
# print(compte_en_banque)
# print(amis)
# print(parents)
#
# #Exo2
#
# site_web = "voila"
# print(str(site_web))
#
# #Exo3
#
# nombre = 15
# print("Le nombre est " + str(nombre))
#
# #Exo 5
#
# a = 2
# b = 6
# c = 3
#
# print(str(a) + ' + ' + str(b) + ' + ' + str(c))
# print(a, b, c, sep=" + ")


# #Exo 6

liste = range(3)
list2 = range(5)

print(list(list2))

# Exo7

prenom = "Pierre"

if type(prenom) == str:
    isString = True
    print(prenom)
else:
    isString = False
    print("Nope :( ")

prenom2 = 0
if isinstance(prenom2, str):
    print("C'est une chaîne !")
else:
    print(prenom2)

# créer un programme qui permet à l'utilisateur de choisr le type à tester

# Exo 8

phrase = "Bonjour les amis"
nouvelle_phrase = phrase.replace("Bonjour", "Salut")

print(nouvelle_phrase)
