import os
import json
import pandas as pd

data_list = []

for filename in os.listdir():
    if filename.endswith(".json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                ptm = data.get("ptm")
                iptm = data.get("iptm")
                data_list.append({
                    "filename": filename,
                    "pTM": ptm,
                    "ipTM": iptm
                })
        except Exception as e:
            print(f"Error processing {filename}: {e}")

df = pd.DataFrame(data_list)
df.to_excel("250925_all-contact-residues-boltz.xlsx", index=False)
