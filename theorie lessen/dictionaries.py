#uitleg
#ieder persoon heeft een speciale key, een rijkregeisternummer

lijst_namen = ["Jarne", "Jarne"]
woordenboek_namen = {19283:"Jarne",
                     1873: "Thomas",
                     1234: "Serhat",}

#als we nu naar een key zoeken zullen we de juiste waarde krijgen

print(woordenboek_namen[1873])

#we voegen iets bij
woordenboek_namen[1029] = "Jef"

print(woordenboek_namen[1029])

#extra functies
'woordenboek_namen.' #zoek zo alle functies
print(list(woordenboek_namen.keys()))

#om iets bepaald te krijgen kun je list(dictionary.keys())[n]
#.values geeft ons alle namen

#iteratie
for i in woordenboek_namen.values():
    print(i)
#of
for i in woordenboek_namen.values():
    print(i)

#om een lijst van tupels te krijgen:
print(woordenboek_namen.items())

#loopen hiermee

for key,value in woordenboek_namen.items():
    print(f'{value}, {key}')

#een dictionary kan nog veel complexer worden dan gewoon woorden en getallen
nummerplaat_woordenboek = {"1-ABC-123":["Serhat",'Murat',"Cevdet"],
                           "1-abc-333":["jef", "Thom", "mat"],
                           123:True,
                           666:"bad"}
#je kunt dus een mix van elementen doen

#hoe verwijder je een element
del nummerplaat_woordenboek[123]

#de items hebben geen volgorde en hun volgorde maakt hier niet uit, dus indexing gaat niet direct hier

nummerplaat_woordenboek[666] = "a"
#er komt nu geen nieuwe item maar een al bestaand item zal gewijzigd worden
