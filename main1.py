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
chaine_1 = input("entrez une chaine de caractere")
chaine_avec_majuscules = chaine_1.title()
print(chaine_avec_majuscules)


#4 Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
texte = input("Entrez une exemple de texte")
mots = texte.split()  
resultat = ''.join([mot[0] for mot in mots])  
print(resultat) 

#5Ranplase tout karaktè "a" ki nan yon chenn pa "@"
texte_2= input("entrez une chaine de caractere")
chaine_modifiee = texte_2.replace('a', '@')
print(chaine_modifiee)


#6Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
Chaine_3= input("Tapez une chaine de caracteres:")
chaine_inverse = Chaine_3[::-1]
chaine_majuscules = chaine_inverse.upper()
print(chaine_majuscules)

#7Afiche endeks premye karaktè "a" ki nan yon chenn. Ekzanp:

texte_4 = input("entrez une chaine de caracteres avec plusieurs a")

index = texte_4.find('a')
 
if index != -1:
    print(f"L'index du premier 'a' est {index}")
else:
    print("Le caractère 'a' n'a pas été trouvé dans la chaîne.")

#8Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil)
texte_5= input("entrez une chaine")

indices_a = []

for i, caractere in enumerate(texte_5):
    if caractere == 'a':
        indices_a.append(i)

total_indices = len(indices_a)

if total_indices > 0:
    print(f"Indices des caractères 'a' : {indices_a}")
    print(f"Total des indices : {total_indices}")
else:
    print("Le caractère 'a' n'a pas été trouvé dans la chaîne.")

#9Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil)
chenn = input("entrez u texte:")

endeks_a = [i for i, karakte in  enumerate(chenn) if karakte == 'a']

print(endeks_a)

#10Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo)


chenn_2= input("Entrez une chaine de caracteres")
chaine_sans_espaces = chenn_2.replace(" ", "")
longueur_chaine = len(chaine_sans_espaces)
print(chaine_sans_espaces)
print(longueur_chaine)

