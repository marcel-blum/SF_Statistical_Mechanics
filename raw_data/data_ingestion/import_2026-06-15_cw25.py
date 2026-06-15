# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 25 of 2026

date_val = "2026-06-15" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw25_2026 = {
    "Paladin":501,
    "Tao":535,
    "StupidHoe":465,
    "Falke":517,
    "Wutbob":518,
    "Bluex3":499,
    "Liiight":493, #inactive
    "Dalle":488,
    "Sharandra":493,
    "Sigurlasius":475,
    "Kampfbock":471,
    "Russischer Golum":467,
    "Raguos":459,
    "Pauliv4":460,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":456,
    "Wolff0303":455,
    "Fasta":461,
    "Swagboi":452,
    "FrankoSan":453,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":454,
    "Hawi":450,
    "Restless":450,
    "Schmollutz":444,
    "ShangriLa":442,
    "CortaX":441,
    "Flosse97":443,
    "Nitzodon Oworotz":437,
    "HER-WIEDZMIN":432,
    "Borán":436,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":437,
    "Liltwo":432,
    "Twerkelele":433,
    "Otis":430,
    "Sunudon Juckamas":430,
    "Dimonz":425,
    #"AndréDE":416, #cw19 #inactive
    "Feye":422,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":421,
    "tris":420,
    #"Annatar":415, #cw21 #inactive
    "Melanie":417,
    "Jan284":417,
    "Psychotherapeut":411,
    "Tecanite":413,
    "Chr1s":406,
    "Szamil":408,
    "Thorgrim":398,
    "BeTaMarci0":398,
    "Dr Gallo":396,
    "Fendo1982":395,
    "CaRRieR":388,
    "Georgie":387,
    "Firsen":377
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw25_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()