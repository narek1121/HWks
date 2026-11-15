import json

students = [
    {"name": "Anna", "score": 85, "level": "B2"},
    {"name": "Ivan", "score": 72, "level": "B1"},
    {"name": "Olga", "score": 91, "level": "C1"},
]

with open("students.json", "w", encoding="utf-8") as f:
    # сохраняем весь список студентов в формате JSON
    json.dump(students, f, ensure_ascii=False, indent=2)
