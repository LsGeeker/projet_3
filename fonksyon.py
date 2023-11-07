import random
import string
import re

#1 kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la
def inverse_mot(mot):
 mot_inverse = mot[::-1]
 return mot_inverse

mot_corrige = inverse_mot("corigee")
print(mot_corrige)

#2 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik
def jenere_kod(n):
    caract_alfa = string.ascii_lowercase
    kod = ''.join(random.choice(caract_alfa) for i in range(n))
    return kod

n = 8 
kod_al = jenere_kod(n)
print(kod_al)

#3 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon
def gene_kod(n):
    karak_alfa = list (string.ascii_lowercase)
    kode = ''.join(random.sample(karak_alfa, n))
    return kode

n = 20
kodal = jenere_kod(n)
print(kodal)

#4 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon
def jenekod(n):
    carak_alfanimerik = string.ascii_letters + string.digits
    kd = ''.join(random.sample(carak_alfanimerik,n))
    return kd
n = 30
code_al = jenekod(n)
print(code_al)

#5 Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"

def generer_slug(chaine):

    chaine_sans_caracteres_non_conformes = re.sub(r'[^a-zA-Z0-9-]', '-', chaine)
    
    
    slug = '-'.join(chaine_sans_caracteres_non_conformes.split('-'))
    
    
    return slug.lower()

chaine = "Une Chaîne avec des Caractères Non-Acceptables!#"
slug = generer_slug(chaine)
print(slug)


#6 Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe_lett_ak_vijil(mot):
    mo_separe = ' '.join(list(mot))
    return mo_separe

mot = "Hello"
mo_separe = separe_lett_ak_vijil(mot)
print(mo_separe)

#7 Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
def kripte_avek_endeks(mot):
 mo_kripte = '-'.join([str(ord(lettre) - ord('A')) for lettre in mot])
 return mo_kripte

mot = "ALO"
mo_kripte = kripte_avek_endeks(mot)
print(mo_kripte)

#8Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.

def dekripte_avek_endeks(mot_kripte):
    endeks_lèt = mot_kripte.split('-')
    mo_dekripte = ''.join([chr(int(endeks) + ord('A')) for endeks in endeks_lèt])
    return mo_dekripte

mot_kripte = "0-11-14"
mo_dekripte = dekripte_avek_endeks(mot_kripte)
print(mo_dekripte)

#9 Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.

def retounen_2_valè(paramèt1, paramèt2):
    return (paramèt1, paramèt2)

valè1 = "Premye valè"
valè2 = 42

rezilta = retounen_2_valè(valè1, valè2)
print(rezilta)

#10 ################
def inisyal_non(non):
    non_divize = non.split('-')  # Divize non an si gen tirè
    inisyal = ''.join([mot[0] for mot in non_divize])
    return inisyal

non = "Jean-Baptiste Jean"
inisyal = inisyal_non(non)
print(inisyal)



