def mask_account_card(card_or_account: str) -> str:
    """
    Функция принимает на вход информацию о карте или счете и возвращает зашифрованную информацию
    """
    list_card_or_account: list = card_or_account.split()

    # Обработка карты
    if list_card_or_account[0] in ["Visa", "MasterCard", "Maestro"]:
        # Шифруем номер карты
        list_card_or_account[-1] = f"{list_card_or_account[-1][:6]}******{list_card_or_account[-1][-4:]}"

        # Оборачиваем номер карты в список для перебора и вставки пробелов
        list_number_card_account = list(list_card_or_account[-1])
        counter = 0
        for index in range(1, len(list_number_card_account)):
            if index % 4 == 0:
                list_number_card_account.insert(index + counter, " ")
                counter += 1
        # Заменяем исходную строку с номером карты на зашифрованную с пробелами
        else:
            list_card_or_account[-1] = "".join(list_number_card_account)
    # Обработка счета
    elif list_card_or_account[0] == "Счет":
        list_card_or_account[-1] = f"**{list_card_or_account[-1][-2:]}"
    # Прочие случаи
    else:
        return "Не верно введенный номер счета или карты"
    return " ".join(list_card_or_account)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Карта"))
