# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 20 of 2026

date_val = "2026-05-18" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw21_2026 = {
    "Paladin":497,
    "Tao":532,
    "StupidHoe":461,
    "Falke":512,
    "Wutbob":513,
    "Bluex3":497,
    "Liiight":491,
    "Sharandra":488,
    "Sigurlasius":471,
    "Kampfbock":466,
    "Russischer Golum":463,
    "Raguos":456,
    "Pauliv4":454,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":451,
    "Wolff0303":451,
    "Fasta":450,
    "Swagboi":450,
    "FrankoSan":449,
    "manekk":447,
    "Bumblebee Hummel":448,
    "Hawi":445,
    "Restless":446,
    "Schmollutz":442,
    "ShangriLa":440,
    "CortaX":439,
    "Flosse97":439,
    "Nitzodon Oworotz":433,
    "HER-WIEDZMIN":429,
    "Borán":431,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":430,
    "Liltwo":427,
    "Twerkelele":429,
    "Otis":428,
    "Sunudon Juckamas":425,
    "Dimonz":421,
    #"AndréDE":416, #cw19 #inactive
    "Feye":419,
    "Krazy Kris":419,
    "Lucario95":417,
    "tris":416,
    #"Annatar":415, #cw21 #inactive
    "Melanie":414,
    "Jan284":413,
    "Psychotherapeut":408,
    "Tecanite":409,
    "Chr1s":404,
    "Szamil":402,
    "Thorgrim":392,
    "BeTaMarci0":390,
    "CaRRieR":385,
    "Georgie":384,
    "Firsen":370
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw21_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()