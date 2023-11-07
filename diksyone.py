#1 Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè
diksyone = {'janvier': 1, 'fevriye': 2, 'mas': 3, 'avril': 4, 'me': 5}

lis_valè = list(diksyone.values())

print(lis_valè)

#2 Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
val = input("entrez une valeur:")
if '{' in val and '}' in val:
    print("cette valeur comprend  des accolades")
    
else:
    print("cette valeur ne comprend pas d'accolades")
 
 #3 Pakouri yon diksyonè, epi afiche tout kle yo
pakou = {'prenom': 'Jean', 'nom': 'Dupont', 'age': 30, 'ville': 'Paris'}

kle = list(pakou.keys())

print(kle)

#4 Pakouri yon diksyonè, epi afiche tout valè yo.
pakouri = {'prenom': 'Jean', 'nom': 'Dupont', 'age': 30, 'ville': 'Paris'}

klef = list(pakouri.values())

print(klef)    

#5Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.

dictionnaire = {'prenom': 'Jean', 'nom': 'Dupont', 'age': 30, 'ville': 'Paris'}
dik ={}
for el, vale in dictionnaire.items():
    dik[el] = vale
print("copie de mon dictionnaire:",dik)

#6#################################
diksyoner = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}

for kle, valè in diksyoner.items():
    if isinstance(valè, str):
        diksyoner[kle] = f"_{valè}_"

print(diksyoner)

#7#############################
diksyone00 = {"a": "12", "b": "abc", "c": "12r", "d": "90"}

nouvo_diksyone001 = {cle: valè for cle, valè in diksyone00.items() if valè.isdigit()}

print(nouvo_diksyone001)

#8 #############################
diksyonè = {"a": 1, "b": 2}

lis_resultat = [(cle, valè) for cle, valè in diksyonè.items()]

print(lis_resultat)

#9##########################
lis_tipl = [("a", 1), ("b", 2)]

diksyonèr = dict(lis_tipl)

print(diksyonèr)


#10 ######################
diksyone1 = {
    "a": 1,
    "b": "koulè",
    "c": [3, 4],
    "d": {5, 6}
}

diksyone2 = {
    "a": 2,
    "b": " blan",
    "c": [7, 8],
    "e": "valè nouvo"
}

nouvo_diksyone = {}

for kle, valè in diksyone1.items():
    tip_valè = type(valè)

    if tip_valè == int:
        nouvo_diksyone[kle] = valè + diksyone2.get(kle, 0)
    if tip_valè in [str, list, set]:
        nouvo_diksyone[kle] = str(valè) + str(diksyone2.get(kle, ''))
    
print(nouvo_diksyone)

