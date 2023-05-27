#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def read_names(filename):
    with open(filename) as f:
        namedata = csv.reader(f, delimiter=";")
        next(namedata)  # ignore header
        return {line[0]: int(line[1].replace(u"\U000000A0", "")) for line in namedata}


miesten_ekat = read_names("etunimitilasto-2023-02-03-dvv/Miehet ens-Table 1.csv")
naisten_nimet = read_names("etunimitilasto-2023-02-03-dvv/Naiset kaikki-Table 1.csv")

nimet = {nimi: (miehet, nimi in naisten_nimet and naisten_nimet[nimi] or 0) for nimi, miehet in miesten_ekat.items()}

konsonantit = "bcdfghjklmnpqrstvwxz"

erikseen_sallitut = set([
    'Aapa',
    'Oku',
    'Puro',
    'Taku',
])

poissuljetut = set([
    'Aake',
    'Aaku',
    'Aale',
    'Aape',
    'Aapeli',
    'Aapi',
    'Aare',
    'Aari',
    'Aarto',
    'Aatami',
    'Aate',
    'Aati',
    'Ahti',
    'Ahto',
    'Ailo',
    'Ailu',
    'Aito',
    'Ake',
    'Akira',
    'Ako',
    'Akseli',
    'Aksu',
    'Akusti',
    'Alaa',
    'Ale',
    'Alho',
    'Ali',
    'Alpi',
    'Alvari',
    'Alvaro',
    'Alve',
    'Alvi',
    'Amine',
    'Ano',
    'Ante',
    'Antero',
    'Anto',
    'Antoni',
    'Ara',
    'Are',
    'Arho',
    'Arimo',
    'Arjo',
    'Arlo',
    'Armo',
    'Arni',
    'Aro',
    'Arvi',
    'Arvo',
    'Arseni',
    'Arsi',
    'Artemi',
    'Asa',
    'Asla',
    'Asmo',
    'Aso',
    'Asseri',
    'Ate',
    'Atle',
    'Atro',
    'Auno',
    'Auvo',
    'Eeka',
    'Eeki',
    'Eemeli',
    'Eemi',
    'Eemu',
    'Eepi',
    'Eeri',
    'Eeti',
    'Eilo',
    'Einari',
    'Eki',
    'Eli',
    'Elia',
    'Elja',
    'Elmeri',
    'Elmo',
    'Elo',
    'Emile',
    'Emilio',
    'Emre',
    'Ensi',
    'Ensio',
    'Ere',
    'Ermo',
    'Erno',
    'Erpo',
    'Ervo',
    'Iiro',
    'Iisko',
    'Iivari',
    'Iivo',
    'Ilari',
    'Ilia',
    'Ilja',
    'Ilmari',
    'Ilmo',
    'Ilo',
    'Immo',
    'Imre',
    'Into',
    'Iouri',
    'Isko',
    'Ismo',
    'Iurii',
    'Ivo',
    'Kaapro',
    'Kaarle',
    'Kaarlo',
    'Kaino',
    'Kajo',
    'Kaleva',
    'Kalevi',
    'Kare',
    'Karlo',
    'Karo',
    'Kassu',
    'Kauno',
    'Kauri',
    'Keimo',
    'Keni',
    'Kirka',
    'Kirmo',
    'Kivi',
    'Kosmo',
    'Kosti',
    'Kouta',
    'Kristo',
    'Kuisma',
    'Kunto',
    'Kustaa',
    'Kusti',
    'Kuuno',
    'Lari',
    'Launo',
    'Leimu',
    'Lenna',
    'Lenne',
    'Lennu',
    'Levi',
    'Lino',
    'Lio',
    'Loke',
    'Louie',
    'Love',
    'Luke',
    'Mainio',
    'Malte',
    'Manne',
    'Manu',
    'Mario',
    'Marlo',
    'Masa',
    'Masi',
    'Mateo',
    'Matheo',
    'Matvei',
    'Maunu',
    'Mauro',
    'Meo',
    'Mertsi',
    'Mete',
    'Miiko',
    'Miilo',
    'Miio',
    'Miiro',
    'Miitri',
    'Mike',
    'Miko',
    'Miku',
    'Milko',
    'Milo',
    'Mino',
    'Mio',
    'Mirko',
    'Miro',
    'Misa',
    'Misha',
    'Miska',
    'Miso',
    'Mitja',
    'Mitri',
    'Mitro',
    'Muisto',
    'Musa',
    'Nemo',
    'Neo',
    'Niila',
    'Niki',
    'Nikita',
    'Nikola',
    'Niku',
    'Nilo',
    'Nima',
    'Nino',
    'Niro',
    'Nisse',
    'Noa',
    'Nooa',
    'Nuka',
    'Nuno',
    'Nuuti',
    'Ohto',
    'Oke',
    'Oki',
    'Ola',
    'Olavi',
    'Ole',
    'Oma',
    'Ora',
    'Orvo',
    'Osama',
    'Oskari',
    'Osku',
    'Osma',
    'Osmo',
    'Otava',
    'Otso',
    'Oula',
    'Ove',
    'Paolo',
    'Pate',
    'Paulo',
    'Pauno',
    'Peitsa',
    'Penna',
    'Pepe',
    'Pessi',
    'Petja',
    'Petro',
    'Pieti',
    'Pietro',
    'Pietu',
    'Poju',
    'Saarni',
    'Sakari',
    'Sakri',
    'Salomo',
    'Sameli',
    'Sampo',
    'Sampsa',
    'Samu',
    'Samuli',
    'Sante',
    'Sasa',
    'Sasha',
    'Saska',
    'Sasu',
    'Savva',
    'Seemi',
    'Seeti',
    'Semi',
    'Severi',
    'Silvo',
    'Sisu',
    'Soini',
    'Soni',
    'Steve',
    'Sture',
    'Sulevi',
    'Sulho',
    'Sulo',
    'Sumu',
    'Sune',
    'Svante',
    'Taavi',
    'Taha',
    'Tahvo',
    'Taimo',
    'Taisto',
    'Taito',
    'Taneli',
    'Tani',
    'Tanu',
    'Tapani',
    'Taro',
    'Tarvo',
    'Tatu',
    'Tauno',
    'Teijo',
    'Tenho',
    'Teo',
    'Terje',
    'Terjo',
    'Terno',
    'Teuvo',
    'The',
    'Theo',
    'Thure',
    'Tiko',
    'Tino',
    'Tito',
    'Toimi',
    'Toma',
    'Tommie',
    'Tore',
    'Torsti',
    'Touho',
    'Tuisku',
    'Ture',
    'Turo',
    'Tuure',
    'Uki',
    'Ukri',
    'Uno',
    'Untamo',
    'Unto',
    'Uolevi',
    'Upi',
    'Urho',
    'Urpo',
    'Usko',
    'Uula',
    'Uuno',
    'Vaito',
    'Valeri',
    'Valio',
    'Valte',
    'Valto',
    'Varma',
    'Vasili',
    'Veerti',
    'Veetu',
    'Veijo',
    'Veini',
    'Veino',
    'Veka',
    'Velmu',
    'Velu',
    'Venne',
    'Venni',
    'Vennu',
    'Verne',
    'Viima',
    'Viki',
    'Vilho',
    'Vili',
    'Viljo',
    'Vilko',
    'Vinski',
    'Visa',
    'Vitali',
    'Vito',
    'Voima',
])

sallivat_suotimet = [
    lambda n, _: n in erikseen_sallitut,  # erikseen sallitut
]

poissulkevat_suotimet = [
    lambda n, yleisyys: yleisyys[0] < 20 or yleisyys[0] >= 7200,  # liian harvinaiset ja suositut pois
    lambda n, yleisyys: yleisyys[1] > 3 * yleisyys[0],  # naisia paljon enemmän kuin miehiä
    lambda n, _: len(n) < 3 or len(n) > 6,  # lyhyet ja pitkät pois
    lambda n, _: n[0].lower() in "hjr",  # Kielletyt alkukirjaimet
    lambda n, _: n[-1] in konsonantit,  # päättyy konsonanttiin
    lambda n, _: any(c in n.lower() for c in "bcdéfgqwxzyöäå"),  # kielletyt kirjaimet
    lambda n, _: any(s in n.lower() for s in ["kk", "ll", "pp", "rn", "rr", "tt"]),  # kielletyt kirjainyhdistelmät
    lambda n, _: n in poissuljetut,  # poissuljetut
]

filtered = {nimi: yleisyys for nimi, yleisyys in nimet.items()
            if any(f(nimi, yleisyys) for f in sallivat_suotimet)
            or all(not f(nimi, yleisyys) for f in poissulkevat_suotimet)}

print(f"{'Nimi':6} {'Miehiä':6} {'Naisia':6}")
print(f"{'----':6} {'------':6} {'------':6}")
for nimi, (m, n) in sorted(filtered.items()):
    print(f"{nimi:6} {m:6} {n:6}")
print(f"Yhteensä {len(filtered)} nimeä")
