from typing import Any

from src.decorators import log


def test_log_terminal_ok(capsys: Any) -> None:
    @log()
    def example_1(x: list) -> Any:
        return x[0]

    example_1([1, 2, 3])
    capture = capsys.readouterr()
    assert capture.out == "example_1 ok\n"


def test_log_terminal_error(capsys: Any) -> None:
    @log()
    def example_2(x: list) -> Any:
        return x[0]

    example_2(0)
    capture = capsys.readouterr()
    assert capture.out == "example_2 'int' object is not subscriptable Inputs: ((0,), {})\n"


def test_log_file_ok() -> None:
    @log(filename="test_ok.txt")
    def example_3(x: list) -> Any:
        return x[0]
    log_path = "logs/test_ok.txt"
    with open(log_path, "w"):
        pass
    example_3([1, 2, 3])
    with open(log_path, "r") as file:
        assert file.read() == "example_3 ok\n"


def test_log_file_error() -> None:
    @log(filename="test_error.txt")
    def example_4(x: list) -> Any:
        return x[0]
    log_path = "logs/test_error.txt"
    with open(log_path, "w"):
        pass
    example_4(0)
    with open(log_path, "r") as file:
        assert file.read() == "example_4 'int' object is not subscriptable Inputs: ((0,), {})\n"
