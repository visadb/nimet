#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

# todo: yleisyys 2020-perusteella

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
])

ei_etunimeksi = set([
    'Aalto',
    'Kaiku',
    'Kuura',
    'Puro',
    'Valo'
])

poissuljetut = set([
    'Aake',
    'Aaku',
    'Aale',
    'Aape',
    'Aapeli',
    'Aapi',
    'Aapo',
    'Aare',
    'Aari',
    'Aaro',
    'Aarto',
    'Aatami',
    'Aate',
    'Aati',
    'Aatu',
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
    'Alpo',
    'Alvari',
    'Alvaro',
    'Alve',
    'Alvi',
    'Ami',
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
    'Arseni',
    'Arsi',
    'Artemi',
    'Arvi',
    'Arvo',
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
    'Eeli',
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
    'Iipo',
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
    'Isto',
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
    'Kimi',
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
    'Lenni',
    'Lennu',
    'Levi',
    'Lino',
    'Lio',
    'Loke',
    'Louie',
    'Love',
    'Luka',
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
    'Miki',
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
    'Oiva',
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
    'Panu',
    'Paolo',
    'Pate',
    'Paulo',
    'Pauno',
    'Peeti',
    'Peetu',
    'Peitsa',
    'Penna',
    'Pepe',
    'Pessi',
    'Pete',
    'Petja',
    'Petro',
    'Pieti',
    'Pietro',
    'Pietu',
    'Poju',
    'Saarni',
    'Sakari',
    'Sakri',
    'Saku',
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
    'Sauli',
    'Savva',
    'Seemi',
    'Seeti',
    'Semi',
    'Severi',
    'Silvo',
    'Sipi',
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
    'Taku',
    'Tami',
    'Taneli',
    'Tani',
    'Tanu',
    'Tapani',
    'Tarmo',
    'Taro',
    'Tarvo',
    'Tatu',
    'Tauno',
    'Teijo',
    'Tenho',
    'Teo',
    'Terho',
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

pisteet = {
    'Aimo'  : (2, 3),
    'Aku'   : (4, 2),
    'Anssi' : (4, 1),
    'Asko'  : (2, 1),
    'Atso'  : (1, 2),
    'Ilpo'  : (2, 1),
    'Kaapo' : (3, 2),
    'Kauko' : (2, 3),
    'Konsta': (2, 2),
    'Lassi' : (5, 2),
    'Leino' : (3, 5),
    'Mauno' : (1, 5),
    'Ossi'  : (4, 3),
    'Timi'  : (3, 1),
    'Topi'  : (5, 2),
    'Touko' : (2, 5)
}

sallivat_suotimet = [
    lambda n, _: n in erikseen_sallitut,  # erikseen sallitut
]

vokaalit = "aeiouyäö"
vokaalieriparit = [a + b for a in vokaalit for b in vokaalit if a != b]

poissulkevat_suotimet = [
    #lambda n, yleisyys: yleisyys[0] < 20 or yleisyys[0] >= 7200,  # liian harvinaiset ja suositut pois
    #lambda n, yleisyys: yleisyys[1] > 3 * yleisyys[0],  # naisia paljon enemmän kuin miehiä
    lambda n, _: len(n) < 3 or len(n) > 6,  # lyhyet ja pitkät pois
    #lambda n, _: n[0].lower() in "hjr",  # Kielletyt alkukirjaimet
    #lambda n, _: n[-1] in konsonantit,  # päättyy konsonanttiin
    lambda n, _: any(c in n.lower() for c in "bcdéfgqwxzyöäå"),  # kielletyt kirjaimet
    #lambda n, _: any(s in n.lower() for s in ["kk", "ll", "pp", "rn", "rr", "tt"]),  # kielletyt kirjainyhdistelmät
    #lambda n, _: n in poissuljetut,
    #lambda n, _: n in ei_etunimeksi,
    # two different consecutive vowels
    lambda n, _: not any(vokaalieripari in n for vokaalieripari in vokaalieriparit),
]

filtered = {nimi: yleisyys for nimi, yleisyys in nimet.items()
            if any(f(nimi, yleisyys) for f in sallivat_suotimet)
            or all(not f(nimi, yleisyys) for f in poissulkevat_suotimet)}

def tuple_sum(tuples):
    return tuple(sum(zipped) for zipped in zip(*tuples))
def nimipalveluyleisyyden_minimi_ja_maksimi(nimipalveluyleisyys):
    if nimipalveluyleisyys == "alle 5":
        return 1, 4
    else:
        return int(nimipalveluyleisyys), int(nimipalveluyleisyys)

def muotoile_vaihteluvali(minimi, maksimi):
    if minimi == maksimi:
        return str(minimi)
    else:
        return f"{minimi}-{maksimi}"
def laske_nimen_yleisyys_alkaen_2010(nimipalvelu_data):
    miehet_min, miehet_max = tuple_sum([nimipalveluyleisyyden_minimi_ja_maksimi(d) for d in [nimipalvelu_data[0], nimipalvelu_data[2]]])
    naiset_min, naiset_max = tuple_sum([nimipalveluyleisyyden_minimi_ja_maksimi(d) for d in [nimipalvelu_data[1], nimipalvelu_data[3]]])
    return muotoile_vaihteluvali(miehet_min, miehet_max), muotoile_vaihteluvali(naiset_min, naiset_max)

def hae_nimen_yleisyysdata_alkaen_2010_nimipalvelusta(nimi):
    cache_file_path = f"nimipalvelu_cache/{nimi}"
    if os.path.isfile(cache_file_path):
        with open(cache_file_path) as f:
            return [l for l in f.read().split("\n") if l]
    else:
        data = os.popen(f"curl -s 'https://verkkopalvelu.vrk.fi/nimipalvelu/nimipalvelu_etunimihaku.asp?L=1' --data-raw 'nimi={nimi}&submit2=HAE'|grep -A12 -e '^2010-19' -e '^2020-'|sed -n -e 5p -e 9p -e 19p -e 23p").read()
        with open(cache_file_path, "w") as f:
            f.write(data)
        return hae_nimen_yleisyysdata_alkaen_2010_nimipalvelusta(nimi)

header = f"{'Nimi':6} {'Miehiä':6} {'Naisia':6}"
#header = f"{'Nimi':6} {'V':1} {'J':1} {'Y':1} {'Miehiä':6} {'Naisia':6} {'Miehiä 2010-':>12} {'Naisia 2010-':>12}"
print(header)
print("-" * len(header))
for nimi, (m, n) in sorted(filtered.items()):
    print(f"{nimi:6} {m:6} {n:6}")
#for nimi, (m, n) in sorted(filtered.items(), key=lambda i: sum(pisteet[i[0]]), reverse=True):
#    miehia_alkaen_2010, naisia_alkaen_2010 = laske_nimen_yleisyys_alkaen_2010(hae_nimen_yleisyysdata_alkaen_2010_nimipalvelusta(nimi))
#    print(f"{nimi:6} {pisteet[nimi][0]} {pisteet[nimi][1]} {sum(pisteet[nimi])} {m:6} {n:6} {miehia_alkaen_2010:>12} {naisia_alkaen_2010:>12}")
print(f"Yhteensä {len(filtered)} nimeä")