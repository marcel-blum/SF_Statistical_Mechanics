# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 18 of 2026

date_val = "2026-04-27" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_q1_2026 = {}

dexterity_q1_2026 = {}

intelligence_q1_2026 = {}

# Levels per week
# change each week
level_cw18_2026 = {
    "Paladin":495,
    "Tao":530,
    "StupidHoe":458,
    "Falke":508,
    "Wutbob":509,
    "Bluex3":493,
    "Liiight":489,
    "Sharandra":485,
    "Sigurlasius":468,
    "Kampfbock":464,
    "Russischer Golum":460,
    "Raguos":454,
    "Pauliv4":452,
    "Bagarrao":450,
    "Bl4ckless":449,
    "Wolff0303":448,
    "Fasta":447,
    "Swagboi":448,
    "FrankoSan":446,
    "Bumblebee Hummel":444,
    "Restless":444,
    "Schmollutz":440,
    "ShangriLa":438,
    "CortaX":437,
    "Flosse97":437,
    "Nitzodon Oworotz":431,
    "HER-WIEDZMIN":428,
    "Borán":427,
    "Major Tom":426,
    "xCanJackson":425,
    "Liltwo":424,
    "Twerkelele":425,
    "Otis":423,
    "Sunudon Juckamas":422,
    "Dimonz":418,
    "AndréDE":416,
    "Feye":416,
    "Krazy Kris":416,
    "Lucario95":415,
    "tris":413,
    "Melanie":411,
    "Jan284":411,
    "Psychotherapeut":407,
    "Tecanite":407,
    "Chr1s":403,
    "Szamil":401,
    "Thorgrim":387,
    "BeTaMarci0":385,
    "CaRRieR":384,
    "Georgie":381,
}

rows = []

for name, val in strength_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_q1_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw18_2026.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

conn.commit()
conn.close()