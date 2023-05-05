def parsing_url(url: str) -> str:
    """
    Функция, возвращающая доменное имя сайта из его URL.
    """
    if '//' in url:  # Если в URL есть протокол передачи данных,
        url = url.split('//')[1]  # то создаем список по разделителю '//' и берем второй элемент
        return url.split('.')[1] if 'www' in url else url.split('.')[0]
    else:
        return url.split('.')[1] if 'www' in url else url.split('.')[0]
