def safe_int(s):
    try:
        # пробуем кастануть
        return int(s)
    except ValueError:
        return None
