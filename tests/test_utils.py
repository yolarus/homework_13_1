from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


def test_get_financial_transactions() -> None:
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
    data = """Этот файл не содержит JSON-строки"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:

        assert get_financial_transactions("test.json") == []
    mock_file.assert_called_once_with("data/test.json", "r")
    capture = capsys.readouterr()
    assert capture.out == "Файл с исходными данными не содержит JSON-строки\n"


def test_get_financial_transactions_without_list(capsys: Any) -> None:
    data = """{}"""
    with patch("builtins.open", mock_open(read_data=data)) as mock_file:

        assert get_financial_transactions("test.json") == []
    mock_file.assert_called_once_with("data/test.json", "r")
    capture = capsys.readouterr()
    assert capture.out == "Файл с исходными данными не содержит список\n"


def test_get_financial_transactions_wrong_filename(capsys: Any) -> None:
    get_financial_transactions("test.json")
    capture = capsys.readouterr()
    assert capture.out == "Неверно указан файл с исходными данными\n"
