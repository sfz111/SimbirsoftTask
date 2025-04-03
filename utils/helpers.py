def evalute_name_to_delete(names: list[str]) -> str:
    """
    Возвращает имя из списка, длина которого ближе всего к средней длине всех имен.
    """
    avg_len = sum([len(name) for name in names]) / len(names)

    min_diff = None
    name_to_delete = names[0]

    for name in names:
        diff = abs(len(name) - avg_len)
        if min_diff is None or diff < min_diff:
            min_diff = diff
            name_to_delete = name

    return name_to_delete


def format_diff(diff: dict) -> str:
    """Форматирование сообщений об ошибке при сравнении json-ов"""

    messages = []
    if 'dictionary_item_removed' in diff:
        for item in diff['dictionary_item_removed']:
            messages.append(f"Отсутствует поле: {item.replace('root', '')}")
    if 'values_changed' in diff:
        for path, change in diff['values_changed'].items():
            messages.append(
                f"Значение поля {path.replace('root', '')} не совпадает: "
                f"ожидалось '{change['old_value']}', получено '{change['new_value']}'"
            )
    return "\n".join(messages)
