# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 20 of 2026

date_val = "2026-05-11" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw20_2026 = {
    "Paladin":496,
    "Tao":532,
    "StupidHoe":459,
    "Falke":511,
    "Wutbob":512,
    "Bluex3":495,
    "Liiight":491,
    "Sharandra":488,
    "Sigurlasius":470,
    "Kampfbock":465,
    "Russischer Golum":461,
    "Raguos":456,
    "Pauliv4":454,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":451,
    "Wolff0303":450,
    "Fasta":450,
    "Swagboi":448,
    "FrankoSan":448,
    "manekk":447,
    "Bumblebee Hummel":447,
    "Hawi":445,
    "Restless":445,
    "Schmollutz":442,
    "ShangriLa":439,
    "CortaX":438,
    "Flosse97":438,
    "Nitzodon Oworotz":433,
    "HER-WIEDZMIN":429,
    "Borán":430,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":429,
    "Liltwo":426,
    "Twerkelele":427,
    "Otis":427,
    "Sunudon Juckamas":425,
    "Dimonz":420,
    #"AndréDE":416, #cw19 #inactive
    "Feye":418,
    "Krazy Kris":417,
    "Lucario95":416,
    "tris":414,
    "Annatar":415,
    "Melanie":413,
    "Jan284":412,
    "Psychotherapeut":408,
    "Tecanite":408,
    "Chr1s":404,
    "Szamil":402,
    "Thorgrim":391,
    "BeTaMarci0":389,
    "CaRRieR":385,
    "Georgie":382,
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw20_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()