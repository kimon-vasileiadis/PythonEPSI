# print('Lets go')
# print('Where ?')

# if 10 > 3:
# print("Mathématiques")

# x = 5
# y = '5'

"""
ici est mon commentaire
"""

# print(y)
# print(x)
# print(str(x)+y)

# x = str(3)
# y = int(3)
# z = float(3)
# a = "salut"
# b = "salut"
#
# print(type(x))
# print(type(y))
# print(type(z))
# print(a)
# print(b)
#
# a=b=c='Hello'
#
# print(a)
# print(b)
# print(c)

# legumes = ["patate", "tomate"]
# a, b = legumes
# print(a)
# print(b)

# x = "Salut"
#
#
# def mafonction():
#     global x
#     x = "superbe"
#
#
# mafonction()
# print("Salut" + x)

# y = 12E4
# print(y)
# z = -50.7e100
# print(z)

# import random
# print(random.randrange(1, 10))
#
# a = "Bonjour"
# print(a[2])
#
# for x in "Salut":
#     print(x)
#
# x = "Voila python"
# print(len(x))

# chaine = "Voila est ce que python"
#
# if "Python" not in chaine:
#     print("Trouvé")
# else:
#     print("Raté")

# b = "Salut les_amis"
# print(b[-5:-2])
# print(b.upper())
# print(b.lower())
#
# c = " Salut les amis "
# print(c.strip())
#
# d = "Salut Python Salut"
# print(d.replace("u", "1", 2))

# e = "Salut, vous"
# print(e.split(","))

# chaine = "Alors qui a vu la série"
# print(chaine)
#
# chaine2 = "Salut\nLes gens"
# print(chaine2)
#
# chaine3 = "Vincent12"
# x = chaine3.isalpha()
# print(x)
#
# print(bool("Yo"))
# print(bool(10))
# print(bool(False))
# print(bool(None))
# print(bool(()))
#
#
# def mafonction():
#     return True
#
#
# print(mafonction())
#
# x = 500
# print(isinstance(x, int))

liste5 = list(("pomme", "fraise", "poire"))
print(liste5)

liste2 =["pomme", "poire", "cerise", "banane", "framboise"]
liste2[1:3] = ["fraise", "ananas"]
print(liste2)

liste3 = ["pomme", "poire", "cerise"]
liste3[1:2] = ["fraise", "ananas"]
print(liste3)

liste3 = ["pomme", "poire", "cerise"]
liste5.insert(2, "fraise")
print(liste5)

liste6 = ["pomme", "poire", "cerise"]
liste6.append("fraise")
print(liste6)

liste7 = ["pomme", "poire", "cerise"]
liste8 = ("orange", "cerise", "fraise")
liste7.extend(liste8)
print(liste8)

