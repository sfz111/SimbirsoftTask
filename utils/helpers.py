def evalute_name_to_delete(names: list[str]) -> str:
    """
    Возвращает имя из списка, длина которого ближе всего к средней длине всех имен.
    """
    names_dict = {name: len(name) for name in names}

    avg_len = sum(names_dict.values()) / len(names)

    min_diff = None
    name_to_delete = names[0]

    for name in names:
        diff = abs(len(name) - avg_len)
        if min_diff is None or diff < min_diff:
            min_diff = diff
            name_to_delete = name

    return name_to_delete
