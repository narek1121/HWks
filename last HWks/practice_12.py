import csv

students = [
    {"name": "Anna", "score": 85},
    {"name": "Ivan", "score": 72},
    {"name": "Olga", "score": 91},
]

with open("report.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    # пишем весь список
    writer.writerows(students)
