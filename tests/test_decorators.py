import os


from src.decorators import log


def test_log_terminal_ok(capsys):
    @log()
    def example_1(x):
        return x[0]

    example_1([1, 2, 3])
    capture = capsys.readouterr()
    assert capture.out == "example_1 ok\n"


def test_log_terminal_error(capsys):
    @log()
    def example_2(x):
        return x[0]

    example_2(0)
    capture = capsys.readouterr()
    assert capture.out == "example_2 'int' object is not subscriptable Inputs: ((0,), {})\n"


"""
def test_log_file_ok(capsys):
    @log(filename="test_ok.txt")
    def example_3(x):
        return x[0]
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("tests_decorators.py"))), "logs/test_ok.txt")
    with open(log_path, "w"):
        pass
    example_3([1, 2, 3])
    with open(log_path, "r") as file:
        assert file.read() == "example_3 ok\n"


def test_log_file_error(capsys):
    @log(filename="test_error.txt")
    def example_4(x):
        return x[0]
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("tests_decorators.py"))), "logs/test_error.txt")
    with open(log_path, "w"):
        pass
    example_4(0)
    with open(log_path, "r") as file:
        assert file.read() == "example_4 'int' object is not subscriptable Inputs: ((0,), {})\n"
"""
