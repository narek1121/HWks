word_count = 0

with open("sample_text.txt", encoding="utf-8") as f:
    # считаем слова во всех строках
    word_count = sum(len(line.split()) for line in f)
