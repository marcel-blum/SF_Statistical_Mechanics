# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 24 of 2026

date_val = "2026-06-08" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw24_2026 = {
    "Paladin":499,
    "Tao":535,
    "StupidHoe":465,
    "Falke":516,
    "Wutbob":516,
    "Bluex3":499,
    "Liiight":493,
    "Sharandra":493,
    "Sigurlasius":474,
    "Kampfbock":469,
    "Russischer Golum":465,
    "Raguos":458,
    "Pauliv4":458,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":455,
    "Wolff0303":453,
    "Fasta":460,
    "Swagboi":452,
    "FrankoSan":452,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":452,
    "Hawi":449,
    "Restless":450,
    "Schmollutz":444,
    "ShangriLa":442,
    "CortaX":441,
    "Flosse97":441,
    "Nitzodon Oworotz":436,
    "HER-WIEDZMIN":431,
    "Borán":435,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":434,
    "Liltwo":431,
    "Twerkelele":432,
    "Otis":430,
    "Sunudon Juckamas":428,
    "Dimonz":424,
    #"AndréDE":416, #cw19 #inactive
    "Feye":422,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":420,
    "tris":419,
    #"Annatar":415, #cw21 #inactive
    "Melanie":416,
    "Jan284":417,
    "Psychotherapeut":409,
    "Tecanite":413,
    "Chr1s":406,
    "Szamil":408,
    "Thorgrim":398,
    "BeTaMarci0":396,
    "Dr Gallo":394,
    "Fendo1982":394,
    "CaRRieR":388,
    "Georgie":387,
    "Firsen":376
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw24_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()