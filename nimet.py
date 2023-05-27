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

filters = [
    lambda n, fr: fr[0] < 20 or fr[0] >= 7200, # liian harvinaiset ja suositut pois
    #lambda n, fr: fr[1] < 5, # naisia vähintään 5
    lambda n, fr: fr[1] > 3*fr[0], # naisia paljon enemmän kuin miehiä
    lambda n, fr: len(n) < 3 or len(n) > 6, # lyhyet ja pitkät pois
    lambda n, fr: n[-1] in "bcdfghjklmnpqrstvwxz", # päättyy konsonanttiin
    #lambda n, fr: any(c in n.lower() for c in ["rtt"]), # kielletyt kirjainyhdistelmät
    lambda n, fr: any(c in n.lower() for c in "bcdéfgqwxzyöäå"), # kielletyt kirjaimet
    lambda n, fr: any(c in n.lower() for c in ["tt"]), # kielletyt kirjainyhdistelmät
    lambda n, fr: n[-2:] in ["ri"],
]

filtered = {nimi: fr for nimi, fr in nimet.items() if all(not f(nimi, fr) for f in filters)}

for nimi, (m, n) in sorted(filtered.items()):
    print(f"{nimi:6} {m:4} {n:4}")
print(f"Yhteensä {len(filtered)} nimeä")
