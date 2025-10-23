import os
import numpy as np
import pandas as pd

data_list = []

for filename in os.listdir():
    if filename.endswith(".npz"):
        try:
            data = np.load(filename)
            ptm = data.get("ptm")
            iptm = data.get("iptm")
            
            ptm_value = float(ptm) if ptm is not None else None
            iptm_value = float(iptm) if iptm is not None else None

            data_list.append({
                "filename": filename,
                "pTM": ptm_value,
                "ipTM": iptm_value
            })
        except Exception as e:
            print(f"Error processing {filename}: {e}")

df = pd.DataFrame(data_list)
df.to_excel("250925_all-contact-residues-chai.xlsx", index=False)
