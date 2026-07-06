# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 27 of 2026

date_val = "2026-07-06" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw28_2026 = {
    "Paladin":503,
    "Tao":538,
    "StupidHoe":510,
    "Falke":523,
    "Wutbob":521,
    "Bluex3":508,
    "Liiight":493, #inactive
    "Dalle":497,
    "Sharandra":497,
    "Sigurlasius":478,
    "Kampfbock":473,
    "Russischer Golum":471,
    "Raguos":462,
    "Pauliv4":463,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":461,
    "Wolff0303":458,
    "Fasta":467,
    "Swagboi":453,
    "FrankoSan":456,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":457,
    "Hawi":454,
    "Restless":453,
    "Schmollutz":446,
    "ShangriLa":444,
    "CortaX":444,
    "Flosse97":445,
    "Nitzodon Oworotz":440,
    "HER-WIEDZMIN":434,
    "Borán":440,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":441,
    "Liltwo":436,
    "Twerkelele":437,
    "Otis":434,
    "Sunudon Juckamas":432,
    "Dimonz":429,
    #"AndréDE":416, #cw19 #inactive
    "Feye":425,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":423,
    "tris":422,
    #"Annatar":415, #cw21 #inactive
    "Melanie":420,
    "Jan284":425,
    "Psychotherapeut":413,
    "Tecanite":415,
    "Chr1s":407,
    "Szamil":410,
    "Thorgrim":404,
    "BeTaMarci0":403,
    "Dr Gallo":397,
    "Fendo1982":401,
    "CaRRieR":389,
    "Georgie":390,
    "Firsen":381
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw28_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()