import os
from functools import wraps
from typing import Any, Callable


def log(*, filename: str = "") -> Callable:
    """
    Формирует журнал вызова функций
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: list, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                result = None
                message = f"{func.__name__} {e} Inputs: {args, kwargs}"
            if filename:
                log_path = os.path.join("logs/", filename)
                if os.path.exists(log_path):
                    marker = "a"
                else:
                    marker = "w"
                with open(log_path, marker) as file:
                    file.write(message + "\n")
            else:
                print(message)
            return result
        return wrapper
    return decorator


"""
if __name__ == "__main__":
    @log(filename="mylog.txt")
    def example_1(x, *, y=1):
        return x[0] * y


    @log()
    def example_2(x):
        return x[0]

    print(example_1([1, 2, 3]))
    print(example_1(0))
    print(example_1([], y=3))
    print(example_2([1, 2, 3]))
    print(example_2([]))
    print(example_2(33))
"""
