import json
import os


def get_financial_transactions(file_name: str) -> list[dict]:
    """
    Функция принимает имя JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(os.path.join("data/", file_name), "r") as data:
            list_of_transactions = json.load(data)
            if isinstance(list_of_transactions, list):
                return list_of_transactions
            else:
                print("Файл с исходными данными не содержит список")
                return []
    except FileNotFoundError:
        print("Неверно указан файл с исходными данными")
        return []
    except json.JSONDecodeError:
        print("Файл с исходными данными не содержит JSON-строки")
        return []
