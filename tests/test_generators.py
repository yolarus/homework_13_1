from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list[dict],
                            filter_by_currency_expected_result: list[dict]) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert result == filter_by_currency_expected_result


def test_filter_by_currency_empty() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions: list[dict]) -> None:
    result = transaction_descriptions(transactions)

    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator() -> None:
    result = card_number_generator(43255678876, 43255678882)
    assert next(result) == "0000 0432 5567 8876"
    assert next(result) == "0000 0432 5567 8877"
    assert next(result) == "0000 0432 5567 8878"


def test_card_number_generator_reverse() -> None:
    result = card_number_generator(43255678882, 43255678876)
    assert next(result) == "0000 0432 5567 8876"
    assert next(result) == "0000 0432 5567 8877"
    assert next(result) == "0000 0432 5567 8878"


def test_card_number_generator_full() -> None:
    result = card_number_generator(4325567887600000, 4325567888200005)
    assert next(result) == "4325 5678 8760 0000"
    assert next(result) == "4325 5678 8760 0001"
    assert next(result) == "4325 5678 8760 0002"
