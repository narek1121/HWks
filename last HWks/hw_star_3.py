import csv
import json

with open("scores.csv", encoding="utf-8", newline="") as f:
    # собираем список словарей через генератор
    result = [{"name": row["name"], "score": int(row["score"])} for row in csv.DictReader(f)]

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
