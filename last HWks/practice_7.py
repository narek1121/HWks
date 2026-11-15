def check_score(score):
    # чекаем диапазон
    if 0 <= score <= 100:
        return score
    raise ValueError("Некорректный балл")
