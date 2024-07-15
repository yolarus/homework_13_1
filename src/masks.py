import logging

from src.decorators import log


masks_logger = logging.getLogger(__name__)
masks_file_formater = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",
    "%d.%m.%Y %H:%M:%S")
masks_file_handler = logging.FileHandler(f'logs/{__name__}.log','w')
masks_file_handler.setFormatter(masks_file_formater)
masks_logger.setLevel(logging.DEBUG)
masks_logger.addHandler(masks_file_handler)


@log(filename="mylog.txt")  # Также решил добавить логирование с помощью декоратора, написанного в прошлом ДЗ
def get_mask_card_number(card_info: list) -> str:
    """
    Функция принимает на вход информацию о карте и возвращает зашифрованную информацию
    """
    # Шифруем номер карты
    masks_logger.info(f"Карта {" ".join(card_info)} передана для шифровки номера")
    card_info[-1] = f"{card_info[-1][:6]}******{card_info[-1][-4:]}"

    # Оборачиваем номер карты в список для перебора и вставки пробелов
    list_card_number = list(card_info[-1])
    counter = 0
    for index in range(1, len(list_card_number)):
        if index % 4 == 0:
            list_card_number.insert(index + counter, " ")
            counter += 1
    # Заменяем исходную строку с номером карты на зашифрованную с пробелами
    else:
        card_info[-1] = "".join(list_card_number)
        masks_logger.info(f"Зашифрованная карта {" ".join(card_info)}")

    return " ".join(card_info)


def get_mask_account(account: list) -> str:
    """
    Функция принимает на вход информацию о счете и возвращает зашифрованную информацию
    """
    masks_logger.info(f"Счет {" ".join(account)} передан для шифровки номера")
    account[-1] = f"**{account[-1][-2:]}"
    masks_logger.info(f"Зашифрованный счет {" ".join(account)}")

    return " ".join(account)


"""
if __name__ == "__main__":
    print(get_mask_card_number("Maestro 1596837868705199".split()))
    print(get_mask_account("Счет 64686473678894779589".split()))
    print(get_mask_card_number("MasterCard 7158300734726758".split()))
    print(get_mask_account("Счет 35383033474447895560".split()))
    print(get_mask_card_number("Visa Classic 6831982476737658".split()))
    print(get_mask_card_number("Visa Platinum 8990922113665229".split()))
    print(get_mask_card_number("Visa Gold 5999414228426353".split()))
    print(get_mask_account("Счет 73654108430135874305".split()))
"""
