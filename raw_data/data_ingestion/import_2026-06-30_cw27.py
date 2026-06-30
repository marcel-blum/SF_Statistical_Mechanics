# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 27 of 2026

date_val = "2026-06-30" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw27_2026 = {
    "Paladin":502,
    "Tao":538,
    "StupidHoe":510,
    "Falke":522,
    "Wutbob":520,
    "Bluex3":506,
    "Liiight":493, #inactive
    "Dalle":494,
    "Sharandra":496,
    "Sigurlasius":477,
    "Kampfbock":471,
    "Russischer Golum":471,
    "Raguos":461,
    "Pauliv4":461,
    #"Bagarrao":450, #cw19 #changed_to_Empire
    "Bl4ckless":459,
    "Wolff0303":457,
    "Fasta":465,
    "Swagboi":452,
    "FrankoSan":455,
    #"manekk":447, #cw22 #changed_to_Empire
    "Bumblebee Hummel":455,
    "Hawi":453,
    "Restless":453,
    "Schmollutz":446,
    "ShangriLa":444,
    "CortaX":443,
    "Flosse97":444,
    "Nitzodon Oworotz":440,
    "HER-WIEDZMIN":434,
    "Borán":439,
    #"Major Tom":426, #cw19 #inactive
    "xCanJackson":439,
    "Liltwo":434,
    "Twerkelele":435,
    "Otis":433,
    "Sunudon Juckamas":430,
    "Dimonz":428,
    #"AndréDE":416, #cw19 #inactive
    "Feye":425,
    #"Krazy Kris":421, #cw24 #changed_to_Frozen_Flames
    "Lucario95":422,
    "tris":422,
    #"Annatar":415, #cw21 #inactive
    "Melanie":419,
    "Jan284":424,
    "Psychotherapeut":412,
    "Tecanite":414,
    "Chr1s":407,
    "Szamil":409,
    "Thorgrim":402,
    "BeTaMarci0":401,
    "Dr Gallo":397,
    "Fendo1982":400,
    "CaRRieR":389,
    "Georgie":389,
    "Firsen":380
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw27_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()