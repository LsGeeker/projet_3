#1mettre les elements en miniscules
chaine = input("Ecrire un mot ou une phrase en majuscules:")
chaine_en_minuscules = chaine.lower()
print(chaine_en_minuscules)

#2Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas

chaine =input ("saisir une chaine de caracteres:")
mots = chaine.split() 
for mot in mots:
     print(mot)


#3Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
chaine = input("entrez une chaine de caractere")
chaine_avec_majuscules = chaine.title()
print(chaine_avec_majuscules)
