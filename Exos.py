import random
from math import *

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

# liste = range(3)
# list2 = range(5)
#
# print(list(list2))
#
# # Exo7
#
# prenom = "Pierre"
#
# if type(prenom) == str:
#     isString = True
#     print(prenom)
# else:
#     isString = False
#     print("Nope :( ")
#
# prenom2 = 0
# if isinstance(prenom2, str):
#     print("C'est une chaîne !")
# else:
#     print(prenom2)

# créer un programme qui permet à l'utilisateur de choisr le type à tester


# Exo 8

# phrase = "Bonjour les amis"
# nouvelle_phrase = phrase.replace("Bonjour", "Salut")
#
# print(nouvelle_phrase)

# programme qui demande a l'utilisateur le nombre d'occurence qu'il veut retirer et demander ce qu'il veut enlever

# string = "que veux tu retirer ?"
# x = input(string)
# while x in string:
#     string.removeprefix(string)
#     print(string)


# liste7 = ["pomme", "poire", "cerise"]
# liste8 = ("orange", "cerise", "fraise")
# liste7.extend(liste8)
#
# for x in liste8:
#     print(x)
#
# for x in range(len(liste8)):
#     print(liste8[x])
#
# x = 0
# while x < len(liste8):
#     print(liste8[x])
#     x = x + 1

# remettre en ordre alphabétique un chaîne de caractère

# chaine = "pomme, abricot, cerise, fraise, orange"
# chaine_liste = chaine.split(", ")
# chaine_liste.sort()
# chaine_en_ordre = ", ".join(chaine_liste)
# print(chaine_en_ordre)
#
#
# créer un programme qui nous permet d'afficher le volume d'un sphère
#
# def spherevolume():
#     rayon = float(input("rayon :"))
#     v = (4 * pi / 3) * (rayon ** 3)
#     print(v)
#
#
# volume = 0
# spherevolume()

""" liste des nombres de 10 a 100"""


# def intlist():
#     liste = []
#     i = 10
#     while len(liste) != 91:
#         liste.append(i)
#         i = i + 1
#     print(liste)
#
#
# intlist()
#
# """ liste des nombres pairs de 1 a 200"""
#
#
# def pairlist():
#     liste = []
#     i = 1
#     while len(liste) != 100:
#         if i % 2 == 0:
#             liste.append(i)
#         i = i + 1
#
#     print(liste)
#
#
# pairlist()
#
#
# def generateDice():
#     length = 0
#     result = 0
#     while length < 10:
#         result = random.randrange(1, 6)
#         length = length + 1
#
#     print(result)
#
#
# generateDice()


# Compter le nombre d'occurences d'une lettre dans une chaine, lowercase and uppercase

def countOccurencesofA():
    lettre_a_chercher = "a"
    phrase = "voila les amis. Alors ça va ?"
    counter = 0
    counter2 = 0

    for lettre_a_chercher in phrase:
        counter = phrase.count(lettre_a_chercher)
        upper = lettre_a_chercher.upper()
        counter2 = phrase.count(upper)

    print(counter + counter2)


countOccurencesofA()

# EXTENSION : Afficher la lettre la plus fréquente d'une chaîne
# EXTENSION 2 : Ajouter dans une chaîne un caractère entre chaque caractère de la chaîne, par exemple la lettre a


# récupérer un élément sur deux de cette liste

liste = [1, 2, 3, 4, 5, 6, 7, 8]
print(liste[::2])
