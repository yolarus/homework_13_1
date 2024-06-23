from typing import List


def filter_by_state(id_info: List[dict], state: str = "EXECUTED") -> List[dict]:
    """
    Функция фильтрует список словарей id с по ключу state
    """
    filter_id_info = []

    for element in id_info:
        if element.get("state") == state:
            filter_id_info.append(element)

    return filter_id_info


def sort_by_date(id_info: List[dict], ascending: bool = True) -> List[dict]:
    """
    Функция сортирует переданные словари по дате. По умолчанию сортировка ведется по возрастанию
    """
    sorted_id_info = sorted(id_info, key=lambda element: element["date"], reverse=ascending)
    return sorted_id_info


if __name__ == "__main__":
    tests_info = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(filter_by_state(tests_info))
    print(filter_by_state(tests_info, "CANCELED"))

    print(sort_by_date(tests_info))
    print(sort_by_date(tests_info, True))
