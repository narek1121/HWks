import json

avg = 0

with open("student.json", encoding="utf-8") as f:
    data = json.load(f)
    # страхуемся, чтобы не поймать ZeroDivisionError
    if data.get("scores"):
        avg = sum(data["scores"]) / len(data["scores"])
