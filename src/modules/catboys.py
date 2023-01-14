import requests
from requests import Response

from src.modules.user import *
from src.utils.colors import ColorCodes
from src.utils.printing import cb_get_input_cat


# Fucking hell
def catboy():
    url: str = "https://api.catboys.com/img"
    req: Response = requests.get(url)
    if req.status_code != 200:
        print("Something went wrong with the request!")
        return

    data = req.json()
    img = data["url"]
    artist = data["artist"]

    return img, artist


def show_catboy() -> None:
    info: tuple[str, str] = catboy()
    print(f"{ColorCodes.MAGENT}Image:{ColorCodes.END} {info[0]}"
          f"\n{ColorCodes.BLUE}Artist:{ColorCodes.END} {info[1]}")

    cb_ans: str = cb_get_input_cat(user.name)
    match cb_ans:
        case 'save':
            if not user.is_logged:
                print("You're not logged in!")
            else:
                user.save_image(info[0])
                show_catboy()
        case 'next':
            show_catboy()
        case 'exit':
            exit_match()
