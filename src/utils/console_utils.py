import os

from termcolor import colored

tab = " " * 4
console_width = os.get_terminal_size().columns


def box(text: list[str] | str) -> str:
    result = ""

    result += "#" * console_width + "\n"

    if type(text) is str:
        text = [text]

    text.insert(0, "")  # type: ignore
    text.insert(len(text), "")  # type: ignore

    for line in text:
        result += line.center(console_width - 2, " ").center(console_width, "#") + "\n"

    result += "#" * console_width

    return result


def center(text: str) -> str:
    return text.center(console_width, " ")


def itemize(lines: list[str]) -> str:
    result = ""

    for i, line in enumerate(lines):
        result += tab + "• " + line + ("\n" if i != len(lines) - 1 else "")

    return result


def clear_terminal() -> None:
    os.system("cls||clear")


def clear_line() -> None:
    print("\033[F\033[K", end="")

def print_error_msg(msg: str, e: Exception) -> None:
    print(colored(center(msg), 'red'))
    print()
    print(tab + "Mensagem de erro:")

    for error_msg_line in str(e).split("\n"):
        print(colored(tab * 2 + error_msg_line, 'red'))

    print()