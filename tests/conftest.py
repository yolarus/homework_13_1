import pytest


@pytest.fixture
def maestro_card_number():
    return "Maestro 1596837868705199"


@pytest.fixture
def masked_maestro_card_number():
    return "Maestro 1596 83** **** 5199"


@pytest.fixture
def visa_card_number():
    return "Visa Classic 6831982476737658"


@pytest.fixture
def masked_visa_card_number():
    return "Visa Classic 6831 98** **** 7658"


@pytest.fixture
def mastercard_card_number():
    return "MasterCard 7158300734726758"


@pytest.fixture
def masked_mastercard_card_number():
    return "MasterCard 7158 30** **** 6758"


@pytest.fixture
def account():
    return "Счет 64686473678894779589"


@pytest.fixture
def masked_account():
    return "Счет **89"
