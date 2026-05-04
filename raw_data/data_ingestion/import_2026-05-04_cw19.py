# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 19 of 2026

date_val = "2026-05-04" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw19_2026 = {
    "Paladin":496,
    "Tao":531,
    "StupidHoe":459,
    "Falke":510,
    "Wutbob":510,
    "Bluex3":494,
    "Liiight":490,
    "Sharandra":487,
    "Sigurlasius":469,
    "Kampfbock":464,
    "Russischer Golum":460,
    "Raguos":454,
    "Pauliv4":453,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":451,
    "Wolff0303":449,
    "Fasta":449,
    "Swagboi":448,
    "FrankoSan":447,
    "manekk":447,
    "Bumblebee Hummel":446,
    "Hawi":444,
    "Restless":444,
    "Schmollutz":441,
    "ShangriLa":439,
    "CortaX":438,
    "Flosse97":438,
    "Nitzodon Oworotz":433,
    "HER-WIEDZMIN":428,
    "Borán":428,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":427,
    "Liltwo":426,
    "Twerkelele":426,
    "Otis":424,
    "Sunudon Juckamas":423,
    "Dimonz":420,
    #"AndréDE":416, #cw19 #inactive
    "Feye":418,
    "Krazy Kris":416,
    "Lucario95":416,
    "tris":414,
    "Annatar":415,
    "Melanie":412,
    "Jan284":412,
    "Psychotherapeut":407,
    "Tecanite":408,
    "Chr1s":404,
    "Szamil":401,
    "Thorgrim":389,
    "BeTaMarci0":387,
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
for name, val in level_cw19_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()