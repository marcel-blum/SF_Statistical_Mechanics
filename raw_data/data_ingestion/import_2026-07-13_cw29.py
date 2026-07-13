# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 29 of 2026

date_val = "2026-07-13" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw29_2026 = {
    "Paladin":503,
    "Tao":539,
    "StupidHoe":511,
    "Falke":523,
    "Wutbob":522,
    "Bluex3":509,
    "Liiight":493, #inactive
    "Dalle":501,
    "Sharandra":497,
    "Sigurlasius":478,
    "Kampfbock":474,
    "Russischer Golum":472,
    "Raguos":464,
    "Pauliv4":463,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":461,
    "Wolff0303":459,
    "Fasta":468,
    "Swagboi":453,
    "FrankoSan":456,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":458,
    "Hawi":456,
    "Restless":455,
    "Schmollutz":447,
    "ShangriLa":445,
    "CortaX":444,
    "Flosse97":445,
    "Nitzodon Oworotz":440,
    "HER-WIEDZMIN":436,
    "Borán":440,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":441,
    "Liltwo":436,
    "Twerkelele":437,
    "Otis":435,
    "Sunudon Juckamas":432,
    "Dimonz":430,
    #"AndréDE":416, #cw19 #inactive
    "Feye":427,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":423,
    "tris":424,
    #"Annatar":415, #cw21 #inactive
    "Melanie":421,
    "Jan284":425,
    "Psychotherapeut":413,
    "Tecanite":416,
    "Chr1s":407,
    "Szamil":411,
    "Thorgrim":404,
    "BeTaMarci0":404,
    "Dr Gallo":399,
    "Fendo1982":402,
    "CaRRieR":389,
    "Georgie":390,
    "Firsen":383
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw29_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()