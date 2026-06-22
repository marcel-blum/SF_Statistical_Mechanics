# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 26 of 2026

date_val = "2026-06-22" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw26_2026 = {
    "Paladin":501,
    "Tao":537,
    "StupidHoe":508,
    "Falke":519,
    "Wutbob":518,
    "Bluex3":506,
    "Liiight":493, #inactive
    "Dalle":489,
    "Sharandra":495,
    "Sigurlasius":476,
    "Kampfbock":471,
    "Russischer Golum":470,
    "Raguos":461,
    "Pauliv4":461,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":457,
    "Wolff0303":456,
    "Fasta":464,
    "Swagboi":452,
    "FrankoSan":453,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":455,
    "Hawi":452,
    "Restless":452,
    "Schmollutz":445,
    "ShangriLa":443,
    "CortaX":443,
    "Flosse97":443,
    "Nitzodon Oworotz":438,
    "HER-WIEDZMIN":434,
    "Borán":438,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":438,
    "Liltwo":433,
    "Twerkelele":433,
    "Otis":432,
    "Sunudon Juckamas":430,
    "Dimonz":427,
    #"AndréDE":416, #cw19 #inactive
    "Feye":424,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":421,
    "tris":421,
    #"Annatar":415, #cw21 #inactive
    "Melanie":418,
    "Jan284":418,
    "Psychotherapeut":412,
    "Tecanite":414,
    "Chr1s":407,
    "Szamil":409,
    "Thorgrim":399,
    "BeTaMarci0":400,
    "Dr Gallo":396,
    "Fendo1982":397,
    "CaRRieR":389,
    "Georgie":388,
    "Firsen":378
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw26_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()