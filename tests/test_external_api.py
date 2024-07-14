from typing import Any
from unittest.mock import patch

from src.external_api import get_sum_of_transaction


@patch("requests.get")
def test_get_sum_of_transaction_usd(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_sum_of_transaction({"operationAmount": {"currency": {"code": "USD"}, "amount": 1}}) == 100
    mock_get.assert_called_once()


def test_get_sum_of_transaction_rub() -> None:
    assert get_sum_of_transaction({"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}) == 100
