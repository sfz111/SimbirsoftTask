def evalute_name_to_delete(names: list[str]) -> str:
    """
    Возвращает имя из списка, длина которого ближе всего к средней длине всех имен.
    """
    names_dict = {name: len(name) for name in names}

    avg_len = sum(names_dict.values()) / len(names)

    minimum = 0
    name_to_delete = ''
    for name, name_len in names_dict.items():
        diff = avg_len - name_len
        if diff <= minimum:
            minimum = diff
            name_to_delete = name

    return name_to_delete
