def move_zeros(array: list) -> list:
    """
    Функция, перемещающая все нули исходного массива в конец,
    не меняя порядок остальных элементов.
    """
    result = [element for element in array if element != 0]  # создаем массив без нулей
    result.extend([0] * (len(array) - len(result)))  # к созданному списку добавляем необходимое кол-во нулей
    return result
