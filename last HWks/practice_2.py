line_count = 0

with open("sample_text.txt", encoding="utf-8") as f:
    # считаем строки на лету
    line_count = sum(1 for _ in f)
