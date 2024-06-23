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

@pytest.fixture
def id_info():
    tests_info = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return tests_info


@pytest.fixture
def filter_executed_id_info():
    tests_info = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    return tests_info


@pytest.fixture
def filter_canceled_id_info():
    tests_info = [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return tests_info


@pytest.fixture
def sort_descending_id_info():
    tests_info = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    return tests_info


@pytest.fixture
def sort_ascending_id_info():
    tests_info = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    return tests_info
