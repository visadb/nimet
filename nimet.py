#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os

def read_names(filename):
    with open(filename) as f:
        namedata = csv.reader(f, delimiter=";")
        next(namedata)  # ignore header
        return {line[0]: int(line[1].replace(u"\U000000A0", "")) for line in namedata}

def lue_sukunimet():
    with open("sukunimitilasto-2023-02-03-dvv/Nimet-Table 1.csv") as f:
        namedata = csv.reader(f, delimiter=";")
        next(namedata)  # ignore header
        return {line[0]: int(line[1].replace(u"\U000000A0", "")) for line in namedata}

#miesten_ekat = read_names("etunimitilasto-2023-02-03-dvv/Miehet ens-Table 1.csv")
miesten_nimet = read_names("etunimitilasto-2023-02-03-dvv/Miehet kaikki-Table 1.csv")
naisten_nimet = read_names("etunimitilasto-2023-02-03-dvv/Naiset kaikki-Table 1.csv")

#sukunimet = lue_sukunimet()
#sukunimietunimet = sorted([(nimi, lkm, sukunimet[nimi]) for nimi, lkm in miesten_ekat.items() if nimi in sukunimet and 5*lkm < sukunimet[nimi] and lkm > 50])
#for nimi, lkm, sukunimet in sukunimietunimet:
#    print(nimi, lkm, sukunimet)

nimet = {nimi: (miehet, nimi in naisten_nimet and naisten_nimet[nimi] or 0) for nimi, miehet in miesten_nimet.items()}

konsonantit = "bcdfghjklmnpqrstvwxz"

with open("poissuljetut.txt") as f:
    poissuljetut = set([nimi.strip() for nimi in f.readlines()])

erikseen_sallitut = set([
])

sallivat_suotimet = [
    lambda n, _: n in erikseen_sallitut,  # erikseen sallitut
]

poissulkevat_suotimet = [
    #lambda n, yleisyys: yleisyys[0] < 20 or yleisyys[0] >= 7200,  # liian harvinaiset ja suositut pois
    lambda n, yleisyys: yleisyys[1] > 3 * yleisyys[0],  # naisia paljon enemmän kuin miehiä
    lambda n, _: len(n) < 5 or len(n) > 9,  # lyhyet ja pitkät pois
    #lambda n, _: n[0].lower() in "hjr",  # Kielletyt alkukirjaimet
    #lambda n, _: n[-1] in konsonantit,  # päättyy konsonanttiin
    lambda n, _: any(c in n.lower() for c in "çébcfgqwxzyöäå-'"),  # kielletyt kirjaimet
    #lambda n, _: any(s in n.lower() for s in ["kk", "ll", "pp", "rn", "rr", "tt"]),  # kielletyt kirjainyhdistelmät
    lambda n, _: n in poissuljetut,
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

header = f"{'Nimi':10} {'Miehiä':6} {'Naisia':6} {'Miehiä 2010-':>12} {'Naisia 2010-':>12}"
print(header)
print("-" * len(header))
for nimi, (m, n) in sorted(filtered.items()):
    miehia_alkaen_2010, naisia_alkaen_2010 = laske_nimen_yleisyys_alkaen_2010(hae_nimen_yleisyysdata_alkaen_2010_nimipalvelusta(nimi))
    print(f"{nimi:10} {m:6} {n:6} {miehia_alkaen_2010:>12} {naisia_alkaen_2010:>12}")
print(f"Yhteensä {len(filtered)} nimeä")