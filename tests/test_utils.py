from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import get_financial_transactions


def test_get_financial_transactions_json() -> None:
    data = """[{"id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58",
                                    "currency": {"name": "руб.",
                                                 "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
                }]"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:

        assert get_financial_transactions("test.json") == [{"id": 441945886,
                                                            "state": "EXECUTED",
                                                            "date": "2019-08-26T10:50:58.294041",
                                                            "operationAmount": {"amount": "31957.58",
                                                                                "currency": {"name": "руб.",
                                                                                             "code": "RUB"}},
                                                            "description": "Перевод организации",
                                                            "from": "Maestro 1596837868705199",
                                                            "to": "Счет 64686473678894779589"
                                                            }]
    mock_file.assert_called_once_with("data/test.json", "r")


def test_get_financial_transactions_without_json(capsys: Any) -> None:
    data = """Файл test.json не содержит JSON-строки"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:

        assert get_financial_transactions("test.json") == []
    mock_file.assert_called_once_with("data/test.json", "r")
    capture = capsys.readouterr()
    assert capture.out == "Файл test.json не содержит JSON-строки\n"


def test_get_financial_transactions_without_list(capsys: Any) -> None:
    data = """{}"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:

        assert get_financial_transactions("test.json") == []
    mock_file.assert_called_once_with("data/test.json", "r")
    capture = capsys.readouterr()
    assert capture.out == "Файл test.json не содержит список\n"


def test_get_financial_transactions_wrong_filename(capsys: Any) -> None:
    get_financial_transactions("test.json")
    capture = capsys.readouterr()
    assert capture.out == "Файл test.json не найден\n"


def test_get_financial_transactions_csv() -> None:
    data = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 1;Счет 2;Перевод организации"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:

        assert get_financial_transactions("test.csv") == [{"id": "650703",
                                                           "state": "EXECUTED",
                                                           "date": "2023-09-05T11:30:32Z",
                                                           "amount": "16210",
                                                           "currency_name": "Sol",
                                                           "currency_code": "PEN",
                                                           "from": "Счет 1",
                                                           "to": "Счет 2",
                                                           "description": "Перевод организации"
                                                           }]
    mock_file.assert_called_once_with("data/test.csv", "r")


def test_get_financial_transactions_other_formats(capsys: Any) -> None:
    data = " "
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:
        assert get_financial_transactions("test.txt") == []
        capture = capsys.readouterr()
        assert capture.out == "Неверный формат файла test.txt\n"
    mock_file.assert_called_once_with("data/test.txt", "r")


@patch("pandas.read_excel")
def test_get_financial_transactions_excel(mock_df: Any) -> None:
    data = " "
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:
        mock_df.return_value = pd.DataFrame({"id": [1, 2, 3, 4, 5]})
        assert get_financial_transactions("test.xlsx") == [{"id": 1},
                                                           {"id": 2},
                                                           {"id": 3},
                                                           {"id": 4},
                                                           {"id": 5}]
        mock_file.assert_called_once_with("data/test.xlsx", "r")
