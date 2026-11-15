import json

en_ru = {"hello": "привет", "cat": "кот", "book": "книга"}

with open("dict.json", "w", encoding="utf-8") as f:
    # дампим с нормальными отступами
    json.dump(en_ru, f, ensure_ascii=False, indent=2)
