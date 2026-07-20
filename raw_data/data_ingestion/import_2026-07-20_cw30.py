# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 30 of 2026

date_val = "2026-07-20" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw30_2026 = {
    "Paladin":504,
    "Tao":542,
    "StupidHoe":513,
    "Falke":525,
    "Wutbob":524,
    "Bluex3":510,
    #"Liiight":493, #inactive
    "Dalle":507,
    "Sharandra":499,
    "Gangsternapper":488,
    "Sigurlasius":479,
    "Kampfbock":474,
    "Russischer Golum":473,
    "Raguos":464,
    "Pauliv4":463,
    "SirAggri":464,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":461,
    "Wolff0303":459,
    "Fasta":468,
    "Swagboi":454,
    "FrankoSan":457,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":459,
    "Hawi":456,
    "Restless":455,
    "Schmollutz":447,
    "ShangriLa":446,
    "CortaX":444,
    "Flosse97":447,
    "Nitzodon Oworotz":441,
    "HER-WIEDZMIN":436,
    "Borán":441,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":442,
    "Liltwo":437,
    "Twerkelele":438,
    "Otis":435,
    "Sunudon Juckamas":433,
    "Dimonz":430,
    #"AndréDE":416, #cw19 #inactive
    "Feye":427,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":424,
    "tris":425,
    #"Annatar":415, #cw21 #inactive
    "Melanie":422,
    "Jan284":427,
    "Psychotherapeut":414,
    "Tecanite":417,
    #"Chr1s":407, #cw29 #inactive
    "Szamil":411,
    "Thorgrim":406,
    "BeTaMarci0":405,
    "Dr Gallo":399,
    "Fendo1982":404,
    #"CaRRieR":389, #cw29 #inactive
    "Georgie":391,
    "Firsen":384
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw30_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()