def get_data(user_date_time: str) -> str:
    """
    Функция принимает строку с датой и временем и возвращает дату
    """
    list_date_time: list = user_date_time.split("T")
    list_date_time[0] = list_date_time[0].split("-")
    format_user_date = ".".join(list_date_time[0][::-1])
    return format_user_date


if __name__ == "__main__":
    print(get_data("2018-07-11T02:26:18.671407"))
