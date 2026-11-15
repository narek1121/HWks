import csv

avg = 0

with open("scores.csv", encoding="utf-8", newline="") as f:
    # сразу вытаскиваем все оценки в список
    scores = [int(row["score"]) for row in csv.DictReader(f)]
    if scores:
        avg = sum(scores) / len(scores)
