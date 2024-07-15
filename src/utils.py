import json
import logging
import os

utils_logger = logging.getLogger(__name__)
utils_file_formater = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",
    "%d.%m.%Y %H:%M:%S")
utils_file_handler = logging.FileHandler(f'logs/{__name__}.log', 'w')
utils_file_handler.setFormatter(utils_file_formater)
utils_logger.setLevel(logging.DEBUG)
utils_logger.addHandler(utils_file_handler)


def get_financial_transactions(file_name: str) -> list[dict]:
    """
    Функция принимает имя JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        utils_logger.info(f"Попытка открыть файл {file_name}")
        with open(os.path.join("data/", file_name), "r") as data:
            utils_logger.info(f"Файл {file_name} успешно открыт")
            list_of_transactions = json.load(data)
            if isinstance(list_of_transactions, list):
                utils_logger.info(f"Файл {file_name} успешно десериализован")
                return list_of_transactions
            else:
                utils_logger.error(f"Файл {file_name} не содержит список")
                print(f"Файл {file_name} не содержит список")
                return []
    except FileNotFoundError:
        utils_logger.error(f"Файл {file_name} не найден")
        print(f"Файл {file_name} не найден")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Файл {file_name} не содержит JSON-строки")
        print("Файл с исходными данными не содержит JSON-строки")
        return []
