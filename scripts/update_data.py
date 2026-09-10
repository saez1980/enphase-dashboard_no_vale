import pandas as pd, re, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
src=ROOT/"Enphase_con_IA.xlsx"
out=ROOT/"data"/"data.json"
df=pd.read_excel(src,sheet_name="Datos")

def num(s):
    m=re.search(r"[-+]?\d+(?:[.,]\d+)?",str(s))
    return float(m.group().replace(".","").replace(",", ".")) if m else 0

rows=[]
for _,r in df.iterrows():
    dt=pd.to_datetime(r["Mes del informe"])
    impm=re.search(r"Imp:\s*([0-9.,]+)",str(r["Energía de red"]))
    expm=re.search(r"Exp:\s*([0-9.,]+)",str(r["Energía de red"]))
    cons=num(r["Consumido"]); imp=num(impm.group(1)) if impm else 0
    rows.append({
      "periodo":dt.strftime("%Y-%m"),"año":int(dt.year),"mes":int(dt.month),
      "produccion":num(r["Producido"]),"consumo":cons,"importada":imp,
      "exportada":num(expm.group(1)) if expm else 0,
      "autoconsumo":round((cons-imp)/cons*100,1) if cons else 0
    })
out.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Actualizados {len(rows)} registros")
