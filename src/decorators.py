import os


from functools import wraps
from typing import Callable, Any


def log(*, filename: str = "") -> Callable:
    """
    Формирует журнал вызова функций
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: list, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    log_path = os.path.join(os.path.dirname(os.path.abspath("")), "logs/", filename)
                    if os.path.exists(log_path):
                        marker = "a"
                    else:
                        marker = "w"
                    with open(log_path, marker) as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    log_path = os.path.join(os.path.dirname(os.path.abspath("")), "logs/", filename)
                    if os.path.exists(log_path):
                        marker = "a"
                    else:
                        marker = "w"
                    with open(log_path, marker) as file:
                        file.write(f"{func.__name__} {e} Inputs: {args, kwargs}\n")
                else:
                    print(f"{func.__name__} {e} Inputs: {args, kwargs}")
                    return None
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
