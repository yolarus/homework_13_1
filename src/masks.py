'''
Работа с зависимостями и виртуальным окружением ведется через Poetry.
Есть файл
.flake8
 с конфигурацией для линтера Flake8.
В
pyproject.toml
 есть конфигурации для
black
,
isort
,
mypy
.
Функции соответствуют PEP 8, имеют аннотации типов, корректный нейминг и docstring.
'''


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску - видны первые 6 и последние 4 цифр
    """
    list_card_number: list = list(str(card_number))
    for index in range(len(list_card_number)):

        if 6 <= index < len(list_card_number) - 4:
            list_card_number[index] = "*"

    counter = 0
    for index in range(1, len(list_card_number)):
        if index % 4 == 0:
            list_card_number.insert(index + counter, " ")
            counter += 1

    return "".join(list_card_number)


def get_mask_account(account: int) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску - видны последние 4 цифр
    """

    list_account: list = list(str(account))
    for index in range(len(list_account)):

        if index < len(list_account) - 4:
            list_account[index] = "*"
    return "".join(list_account)[-6:]


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
