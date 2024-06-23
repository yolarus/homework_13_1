from src.widget import get_data, mask_account_card


def test_get_data():
    assert get_data("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_mask_account_card_maestro(maestro_card_number, masked_maestro_card_number):
    assert mask_account_card(maestro_card_number) == masked_maestro_card_number


def test_mask_account_card_visa(visa_card_number, masked_visa_card_number):
    assert mask_account_card(visa_card_number) == masked_visa_card_number


def test_mask_account_card_mastercard(mastercard_card_number, masked_mastercard_card_number):
    assert mask_account_card(mastercard_card_number) == masked_mastercard_card_number


def test_mask_account_card_account(account, masked_account):
    assert mask_account_card(account) == masked_account


def test_mask_account_card():
    assert mask_account_card("Карта 533") == "Не верно введенный номер счета или карты"
