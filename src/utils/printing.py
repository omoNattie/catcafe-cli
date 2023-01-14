from getpass import getpass

from src.utils.colors import ColorCodes

banned_words: list[str] = ["WHERE", "DROP", "=", "SELECT", "INTO", "INSERT", "VALUES"]


def cb_get_input(name: str) -> str:
    inp: str = input(f"{ColorCodes.GREEN}{name}{ColorCodes.END} -> ")

    if inp in banned_words:
        print("Please do not try to use this command.")
    else:
        return inp


def cb_get_input_cat(name: str) -> str:
    inp: str = input(f"{ColorCodes.GREEN}{name}{ColorCodes.END} (view) -> ")

    if inp in banned_words:
        print("Please do not try to use this command.")
    else:
        return inp


def cb_get_password(name: str) -> str:
    inp: str = getpass(f"{ColorCodes.GREEN}{name}{ColorCodes.END} (pass invis) -> ")

    if inp in banned_words:
        print("Please do not try to use this command.")
    else:
        return inp
