import csv

n_students = 0

with open("scores.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader, None)  # скипаем заголовок
    n_students = sum(1 for _ in reader)
