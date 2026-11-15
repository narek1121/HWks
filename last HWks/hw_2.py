import json

first_name = ""

with open("students.json", encoding="utf-8") as f:
    data = json.load(f)
    # берем имя первого, если список не пустой
    if data:
        first_name = data[0].get("name", "")
