from sqlite3 import Connection

from src.modules.catboys import show_catboy
from src.utils.clear import clear
from src.utils.printing import *
from src.modules.user import *


def main() -> None:
    print("Welcome to the cat cafe cli!\n\n"
          + "Type exit to leave or type login, or register to begin!\n"
          + "Type help for help on how to use this thing!\n")

    while True:
        ans = cb_get_input(user.name)
        match ans:
            case 'exit':
                break

            case 'whoami':
                print(f"Logged in as {user.name}, {user.is_logged}")

            case 'login':
                if not user.is_logged:
                    print("Okay! What's your user name?")
                    uname: str = cb_get_input(user.name)
                    print("Great! Now, what's your password?")
                    passwd: str = cb_get_password(user.name)

                    user.login(uname.strip(), passwd.strip())
                else:
                    print("You're already logged in!")

            case 'logout':
                if user.is_logged:
                    print("We are sorry to see you go!\nBefore you log out, please input your password.")
                    passwd: str = cb_get_password(user.name)

                    cursor: Cursor = connection.cursor()
                    cursor.execute(f"SELECT * FROM Users WHERE Password=?", [passwd])

                    if cursor.fetchone() is not None:
                        user.logout(passwd.strip())
                    else:
                        print("Passwords did not match!")
                else:
                    print("You're not logged in!")

            case 'register':
                if not user.is_logged:
                    print("Okay! What's your user name?")
                    uname: str = cb_get_input(user.name)

                    print("Great! Now, what's your password?")
                    passwd: str = cb_get_password(user.name)

                    print("Please re-enter your password.")
                    repasswd: str = cb_get_password(user.name)

                    if passwd != repasswd:
                        print("Passwords did not match!")
                    else:
                        user.register(uname.strip(), passwd.strip())
                else:
                    print("You're already logged in!")

            case 'catboy':
                print("Press ctrl + left click to access the link.\n")
                show_catboy()

            case 'liked':
                if not user.is_logged:
                    print("You're not logged in!")
                else:
                    user.show_liked()

            case 'help':
                print(help_str)

            case 'clear':
                clear()


if __name__ == '__main__':
    main()
