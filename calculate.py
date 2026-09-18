import csv

WEIGHTS = {"C1":25,"C2":20,"C3":15,"C4":15,"C5":10,"C6":10,"C7":5}
TIEBREAK = ["C1","C4","C3","C2","C5","C6","C7"]

def score(row):
    return round(sum(float(row[c]) / 5 * w for c, w in WEIGHTS.items()))

with open("SCORE_MATRIX.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    calculated = score(row)
    if calculated != int(row["final_score"]):
        raise SystemExit(f'{row["participant"]}: calculated={calculated}, published={row["final_score"]}')

ordered = sorted(
    rows,
    key=lambda r: (-int(r["final_score"]), *[-int(r[c]) for c in TIEBREAK], r["participant"])
)

for rank, row in enumerate(ordered, 1):
    if rank != int(row["rank"]):
        raise SystemExit(f'{row["participant"]}: rank={rank}, published={row["rank"]}')

print("OK: frozen scoring and tie-break reproduced")
