from src.masks import get_mask_account, get_mask_card_number


def get_data(user_date_time: str) -> str:
    """
    Функция принимает строку с датой и временем и возвращает дату
    """
    list_date_time: list = user_date_time.split("T")
    list_date_time[0] = list_date_time[0].split("-")
    format_user_date = ".".join(list_date_time[0][::-1])
    return format_user_date


def mask_account_card(card_or_account: str) -> str:
    """
    Функция принимает на вход информацию о карте или счете и возвращает зашифрованную информацию
    """
    list_card_or_account: list = card_or_account.split()

    # Обработка карты
    if list_card_or_account[0] in ["Visa", "MasterCard", "Maestro"]:
        return get_mask_card_number(list_card_or_account)
    # Обработка счета
    elif list_card_or_account[0] == "Счет":
        return get_mask_account(list_card_or_account)
    # Прочие случаи
    else:
        return "Не верно введенный номер счета или карты"


if __name__ == "__main__":
    print(get_data("2018-07-11T02:26:18.671407"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Карта"))
