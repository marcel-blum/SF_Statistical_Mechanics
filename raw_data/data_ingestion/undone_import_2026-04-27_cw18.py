# load necessary libraries
import pandas as pd
import sqlite3

# data from calendar week 17 of 2026

date_val = "2026-04-20" # change for edit

# attributes per month
# commit empty dictionary after monthly contribution
strength_april26 = {
    "StupidHoe":81957,
    "Wutbob":106604,
    "RussischerGolum":76694,
    "Raguos":59016,
    "FrankoSan":57225,
    "Twerkelele":46900,
    "tris":50453,
    "Jan284":44070,
    "CaRRieR":41906,
    "Georgie":38831
}
#strength_april26 = {}

dexterity_april26 = {
    "Paladin":113935,
    "Tao":162241,
    "Bluex3":115519,
    "Pauliv4":88295,
    "Bumblebee Hummel":53874,
    "Restless":64851,
    "Schmollutz":41306,
    "HER-WIEDZMIN":40932,
    "Melanie":53397,
    "Tecanite":51932,
    "Szamil":36689,
    "Tibi":30122
}
#dexterity_april26 = {}

intelligence_april26 = {
    "Falke":133413,
    "Liiight":115896,
    "Sharandra":85941,
    "Sigurlasius":65283,
    "Kampfbock":66315,
    "Bagarrao":65585,
    "Bl4ckless":82110,
    "Wolff0303":69190,
    "Fasta":42913,
    "Swagboi":58448,
    "ShangriLa":63761,
    "CortaX":57132,
    "Flosse97":55880,
    "Nitzodon Oworotz":59874,
    "Borán":79696,
    "Major Tom":63113,
    "xCanJackson":55033,
    "Liltwo":41969,
    "Otis":49982,
    "Sunudon Juckamas":67156,
    "Dimonz":53325,
    "AndréDE":42195,
    "Feye":52486,
    "Krazy Kris":47871,
    "Lucario95":51287,
    "Psychotherapeut":40323,
    "Chr1s":33232,
    "BeTaMarci0":38840
}
#intelligence_april26 = {}

# Levels per week
# change each week
level_cw17_26 = {
    "Paladin":495,
    "Tao":530,
    "StupidHoe":456,
    "Falke":508,
    "Wutbob":507,
    "Bluex3":491,
    "Liiight":488,
    "Sharandra":484,
    "Sigurlasius":467,
    "Kampfbock":463,
    "Russischer Golum":460,
    "Raguos":453,
    "Pauliv4":451,
    "Bagarrao":450,
    "Bl4ckless":449,
    "Wolff0303":447,
    "Fasta":447,
    "Swagboi":446,
    "FrankoSan":445,
    "Bumblebee Hummel":443,
    "Restless":442,
    "Schmollutz":440,
    "ShangriLa":438,
    "CortaX":437,
    "Flosse97":436,
    "Nitzodon Oworotz":430,
    "HER-WIEDZMIN":428,
    "Borán":426,
    "Major Tom":426,
    "xCanJackson":424,
    "Liltwo":424,
    "Twerkelele":424,
    "Otis":423,
    "Sunudon Juckamas":422,
    "Dimonz":418,
    "AndréDE":416,
    "Feye":416,
    "Krazy Kris":416,
    "Lucario95":415,
    "tris":412,
    "Melanie":411,
    "Jan284":410,
    "Psychotherapeut":407,
    "Tecanite":405,
    "Chr1s":403,
    "Szamil":400,
    "BeTaMarci0":384,
    "CaRRieR":383,
    "Georgie":380,
    "Tibi":375
}

rows = []

for name, val in strength_april26.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Strength"})
for name, val in dexterity_april26.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Dexterity"})
for name, val in intelligence_april26.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Intelligence"})
for name, val in level_cw17_26.items():
    rows.append({"timestamp": date_val, "player_name": name, "value": val, "stat_type": "Level"})


df = pd.DataFrame(rows)

# get data in db
conn = sqlite3.connect("../sf_data.db")
cursor = conn.cursor()
df.to_sql("guild_tracking", conn, if_exists = "append", index = False)

# prevent having duplicates
cursor.execute("""
    DELETE FROM guild_tracking 
    WHERE rowid NOT IN (
        SELECT MIN(rowid) 
        FROM guild_tracking 
        GROUP BY timestamp, player_name, stat_type, value
    )
""")
conn.commit()
conn.close()