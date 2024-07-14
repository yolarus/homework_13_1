import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_info, expected", [("Maestro 1596837868705199".split(),
                                                  "Maestro 1596 83** **** 5199"),
                                                 ("MasterCard 7158300734726758".split(),
                                                  "MasterCard 7158 30** **** 6758"),
                                                 ("Visa Classic 6831982476737658".split(),
                                                  "Visa Classic 6831 98** **** 7658")])
def test_get_mask_card_number(card_info: list, expected: str) -> None:
    assert get_mask_card_number(card_info) == expected


def test_get_mask_account(account: str, masked_account: str) -> None:
    assert get_mask_account(account.split()) == masked_account
