import pytest


from src.masks import get_mask_card_number, get_mask_account

my_list = ["Maestro 1596837868705199",
           "Счет 64686473678894779589",
           "MasterCard 7158300734726758",
           "Счет 35383033474447895560",
           "Visa Classic 6831982476737658",
           "Visa Platinum 8990922113665229",
           "Visa Gold 5999414228426353",
           "Счет 73654108430135874305"
           ]


@pytest.mark.parametrize("card_info, expected", [("Maestro 1596837868705199".split(),
                                                  "Maestro 1596 83** **** 5199"),
                                                 ("MasterCard 7158300734726758".split(),
                                                  "MasterCard 7158 30** **** 6758"),
                                                 ("Visa Classic 6831982476737658".split(),
                                                  "Visa Classic 6831 98** **** 7658")])
def test_get_mask_card_number(card_info, expected):
    assert get_mask_card_number(card_info) == expected


@pytest.mark.parametrize("account, expected", [("Счет 64686473678894779589".split(), "Счет **89"),
                                                 ("Счет 35383033474447895560".split(), "Счет **60")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected