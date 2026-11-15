class EmptyTextError(Exception):
    pass

def analyze_text(text):
    # если строка пустая или одни пробелы
    if not text or not text.strip():
        raise EmptyTextError("Текст пустой")
    return len(text.split())
