import re


def hashtag_generator(string: str) -> str:
    """
    Функция, генерирующая хэштэг по заданной строке.
    """
    if len(string) == 0:
        return False
    words = re.sub(r'[^\w\s]', '', string).title().split()  # Список слов предложения без знаков препинания, каждое слово с большой буквы
    hastag = '#' + ''.join(words)
    if len(hastag) > 140 or len(hastag) == 1:  # в хэштэге всегда есть символ "#", поэтому длина сравнивается с единицей
        return False
    return hastag
