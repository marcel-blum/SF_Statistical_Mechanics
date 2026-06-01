# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 23 of 2026

date_val = "2026-06-01" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw23_2026 = {
    "Paladin":499,
    "Tao":534,
    "StupidHoe":463,
    "Falke":515,
    "Wutbob":515,
    "Bluex3":498,
    "Liiight":493,
    "Sharandra":491,
    "Sigurlasius":473,
    "Kampfbock":468,
    "Russischer Golum":464,
    "Raguos":458,
    "Pauliv4":457,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":454,
    "Wolff0303":453,
    "Fasta":458,
    "Swagboi":450,
    "FrankoSan":450,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":451,
    "Hawi":448,
    "Restless":448,
    "Schmollutz":444,
    "ShangriLa":441,
    "CortaX":441,
    "Flosse97":441,
    "Nitzodon Oworotz":435,
    "HER-WIEDZMIN":431,
    "Borán":433,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":433,
    "Liltwo":430,
    "Twerkelele":430,
    "Otis":430,
    "Sunudon Juckamas":427,
    "Dimonz":423,
    #"AndréDE":416, #cw19 #inactive
    "Feye":421,
    "Krazy Kris":421,
    "Lucario95":420,
    "tris":418,
    #"Annatar":415, #cw21 #inactive
    "Melanie":415,
    "Jan284":415,
    "Psychotherapeut":409,
    "Tecanite":411,
    "Chr1s":405,
    "Szamil":407,
    "Thorgrim":395,
    "BeTaMarci0":394,
    "Dr Gallo":393,
    "CaRRieR":387,
    "Georgie":385,
    "Firsen":373
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw23_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()