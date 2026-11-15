words = ["apple", "banana", "cherry"]

with open("words_out.txt", "w", encoding="utf-8") as f:
    # закидываем слова сразу с переносом строки
    f.writelines(f"{word}\n" for word in words)
