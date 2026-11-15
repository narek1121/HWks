def read_file_safe(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # если файла нет, просто возвращаем None
        return None
