with open("diary.txt", "w", encoding="utf-8") as f:
    # закидываем сразу пачкой
    f.writelines(["Day 1: started Python\n", "Day 2: learned files\n"])

with open("diary.txt", "a", encoding="utf-8") as f:
    f.write("Day 3: finished homework\n")
