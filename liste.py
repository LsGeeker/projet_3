#1Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = 50  # Ou ka chanje n nan vale ou vle
lis_resulta = []

for eleman in range(n + 1):
    if eleman % 2 == 0:
        lis_resulta.append(eleman)

print(lis_resulta)

#2 Ou gen yon lis antye, konvèti l an yon lis chenn.
lis_antye = [1, 2, 3, 4, 5]  #
lis_chenn = [str(eleman) for eleman in lis_antye]  

print(lis_chenn)


#3 Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis_miniskil = ["jan", "fevriye", "mas", "avril", "me", "jiyen"]
lis_majiskil = [mois.upper() for mois in lis_miniskil]
print(lis_majiskil)


#4Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis_done = [10, 20, 30, 40, 50, 60, 70, 80, 90]  # Lis done
lis_resulta = [eleman for i, eleman in enumerate(lis_done) if i % 3 == 0]

print(lis_resulta)


#5 Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl
lis_done1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Lis done
lis_resulta2 = [tuple(lis_done1[i:i+3]) for i in range(0, len(lis_done1), 3)]

print(lis_resulta2)

#6 Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon
liste_done = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]  # Lis done ak eleman ki repete
liste_sans_doublon = list(set(liste_done))

print(liste_sans_doublon)

#7 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo
liste1 = [1, 2, 3, 4, 5]
liste2 = [3, 4, 5, 6, 7]
lis_komen = [eleman for eleman in liste1 if eleman in liste2]

print(lis_komen)

#8Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo

liste_1 = [1, 2, 3, 4, 5]
liste_2 = [3, 4, 5, 6, 7]

lis_distenksyon = list(set(liste_1) ^ set(liste_2))

print(lis_distenksyon)

#9 Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
diksyone = {'janvier': 1, 'fevriye': 2, 'mas': 3, 'avril': 4, 'me': 5}
lis_kle = list(diksyone.keys())
lis_valè = list(diksyone.values())
print("List kle:", lis_kle)
print("List valè:", lis_valè)

#10 Reyini 3 lis ansanm, san okenn doublon.
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis3 = [5, 6, 7, 8, 9]

# Konvèti chak lis nan yon ansanm
ansanm1 = set(lis1)
ansanm2 = set(lis2)
ansanm3 = set(lis3)

# Reyini ansanm yo ansanm
ansanm_reyini = ansanm1.union(ansanm2, ansanm3)

# Konvèti ansanm reyini a nan yon lis
lis_reyini = list(ansanm_reyini)

print(lis_reyini)





