'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "-" * 40
username= {"bob":"123", "ann":"pass123", "mike":"password123","liz":"pass123"}

#vložení jméno

jmeno = input("username:")

#ověření uživatele, vložení hesla

if jmeno in username:
    heslo = input("password:")
else:
    print("unregistered user, terminating the program..")
    quit()

#ověření hesla

if heslo == username.get(jmeno):
    print(oddelovac)
    print(f"Welcome to the app, {jmeno} "
          "We have 3 texts to be analyzed."
          )
else:
    print("incorrect password, terminating the program..")
    quit()

#vybrání textu a ověření hodnot

cislo_textu = input("Enter a number btw. 1 and 3 to select:")


if cislo_textu.isalpha():
    print("choose is not number, quit..")
    quit()
elif cislo_textu not in ("1", "2", "3"):
    print("wrong number, quit.. ")
    quit()
else:
    print(oddelovac)

#převedení čísla textu na index

cislo_textu_index = int(cislo_textu) - 1

vybrany_text = (TEXTS[cislo_textu_index])

#vyčištění textu, odstranění teček a čárek

cisty_text = []

for slovo in vybrany_text.split():
    cisty_text.append(slovo.strip(".,"))

#print(cisty_text)

#počet slov

pocet_slov = len(cisty_text)
print(f"There are {pocet_slov} words in the selected text.")

#počet slov začínajících velkým písmenem,

prvni_velke = []

for slovo in cisty_text:
    if slovo.istitle():
        prvni_velke.append(slovo)

prvni_velke = (len(prvni_velke))

print(f"There are {prvni_velke} titlecase words.")


#počet slov psaných velkými písmeny,

vse_velke = []

for slovo in cisty_text:
    if slovo.isupper():
        if slovo.isalpha():
            vse_velke.append(slovo)

vse_velke = (len(vse_velke))

print(f"There are {vse_velke} uppercase words.")

#počet slov psaných malými písmeny,

vse_male = []

for slovo in cisty_text:
    if slovo.islower():
        vse_male.append(slovo)

vse_male = (len(vse_male))

print(f"There are {vse_male} lowercase words.")

#počet čísel (ne cifer),

vse_cisla = []

for slovo in cisty_text:
    if slovo.isnumeric():
        vse_cisla.append(slovo)

vse_cisla1 = len(vse_cisla)
print(f"There are {vse_cisla1} numeric strings.")


#sumu všech čísel (ne cifer) v textu.

suma_cisel = []
for slovo in vse_cisla:
    suma_cisel.append(int(slovo))

print(f"The sum of all the numbers {sum(suma_cisel)}")

print(oddelovac)

#graf

delka_slov = []
slova_textu = []

for slovo in cisty_text:
    if len(slovo) not in delka_slov:
        delka_slov.append(len(slovo))

for slovo in cisty_text:
    slova_textu.append(slovo)


#print(sorted(delka_slov))
#print(slova_textu)

vyskyt_slov = {}

for slovo in slova_textu:
    if len(slovo) not in vyskyt_slov:
        vyskyt_slov[len(slovo)] = 1
    elif len(slovo) in vyskyt_slov:
        vyskyt_slov[len(slovo)] += 1

vyskyt_slov_tuple = vyskyt_slov.items()

vyskyt_slov_slovnik=vyskyt_slov_tuple

vyskyt_slov_slovnik = sorted(vyskyt_slov_slovnik)

print(f"LEN|     OCCURENCES      |NR.")

for cislo in vyskyt_slov_slovnik:
    pocet_vyskytu = "*" * cislo[1]
    print(f"{cislo[0]:3}| {pocet_vyskytu:20}| {cislo[1]:2}")

print(oddelovac)