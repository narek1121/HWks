import json

def merge_json(path1, path2, out):
    # читаем оба файла
    with open(path1, encoding="utf-8") as f1, open(path2, encoding="utf-8") as f2:
        merged_data = json.load(f1) + json.load(f2)
    
    # сохраняем объединенный результат
    with open(out, "w", encoding="utf-8") as f_out:
        json.dump(merged_data, f_out, ensure_ascii=False, indent=2)
