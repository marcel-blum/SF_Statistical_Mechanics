# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 22 of 2026

date_val = "2026-05-25" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw22_2026 = {
    "Paladin":498,
    "Tao":533,
    "StupidHoe":462,
    "Falke":513,
    "Wutbob":514,
    "Bluex3":498,
    "Liiight":493,
    "Sharandra":490,
    "Sigurlasius":472,
    "Kampfbock":467,
    "Russischer Golum":464,
    "Raguos":456,
    "Pauliv4":457,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":453,
    "Wolff0303":452,
    "Fasta":455,
    "Swagboi":450,
    "FrankoSan":450,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":450,
    "Hawi":447,
    "Restless":447,
    "Schmollutz":442,
    "ShangriLa":441,
    "CortaX":439,
    "Flosse97":440,
    "Nitzodon Oworotz":435,
    "HER-WIEDZMIN":430,
    "Borán":432,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":431,
    "Liltwo":429,
    "Twerkelele":430,
    "Otis":428,
    "Sunudon Juckamas":427,
    "Dimonz":423,
    #"AndréDE":416, #cw19 #inactive
    "Feye":420,
    "Krazy Kris":420,
    "Lucario95":418,
    "tris":417,
    #"Annatar":415, #cw21 #inactive
    "Melanie":414,
    "Jan284":414,
    "Psychotherapeut":409,
    "Tecanite":411,
    "Chr1s":405,
    "Szamil":403,
    "Thorgrim":394,
    "BeTaMarci0":393,
    "Dr Gallo":392,
    "CaRRieR":386,
    "Georgie":385,
    "Firsen":372
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw22_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()