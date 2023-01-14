from sqlite3 import Cursor

from src.utils.database import *

db = DataBase("src/data/users.db")
connection: Connection = db.connect()


class User:
    name = 'Guest'
    is_logged = False

    def login(self, uname: str, passwd: str) -> None:
        cursor: Cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Users WHERE UserName=?", [uname])

        if cursor.fetchone() is None:
            print("User with that name does not exist!")
            return

        res = cursor.execute(f"SELECT Password FROM Users WHERE Password=?", [passwd])
        if res.fetchone() is not None:
            self.name = uname
            self.is_logged = True

            print(f"Done! Logged in as {user.name}")
        else:
            print("Invalid Credentials, Passwords did not match")

    def logout(self, passwd: str) -> None:
        cursor: Cursor = connection.cursor()

        res: Cursor = cursor.execute(f"SELECT Password FROM Users WHERE Password=?", [passwd])

        if res.fetchone() is not None:
            self.name = 'Guest'
            self.is_logged = False

            print(f"Done! Logged out\nYou can now log in again!")
        else:
            print("Invalid Credentials, passwords do not match!")

    @staticmethod
    def register(uname: str, passwd: str) -> None:
        cursor: Cursor = connection.cursor()

        if len(passwd) < 8:
            print("Password must be at least 8 characters long!")
            return

        cursor.execute(f"SELECT * FROM Users WHERE UserName=?", [uname])
        if cursor.fetchone() is not None:
            print(f"User with that name already exists!")
            return

        cursor.execute(f"INSERT INTO Users (UserName, Password, Liked) VALUES (?,?,?)", ([uname], [passwd], ["None"]))
        connection.commit()

        print(f"User {uname} has been registered! Feel free to log in now!")

    def save_image(self, url: str):
        cursor: Cursor = connection.cursor()

        res = cursor.execute("SELECT * FROM Users WHERE UserName=?", [self.name]).fetchone()
        liked_str = res[2]

        if liked_str == "None":
            liked_str = ""

        liked_str += f"{url}\n"
        cursor.execute("UPDATE Users SET Liked=? WHERE UserName=?", [liked_str, self.name])

        connection.commit()

        print("Done!")

    def show_liked(self):
        cursor: Cursor = connection.cursor()

        res = cursor.execute("SELECT * FROM Users WHERE UserName=?", [self.name]).fetchone()
        liked_str = res[2]

        print(liked_str)


user: User = User()
help_str: str = """
Welcome to the cat-cafe cli app!
Where you can find all your catboy needs!
                
Main Commands:
    login       - Log in into your account.
    logout      - Log out of your account.
    register    - Creates a new account.
    whoami      - Shows who you're logged in as.
    catboy      - Shows url of an image of a catboy, using the catboys.com api!
    liked       - Shows the saved picture urls.
    help        - This command.
    clear       - Clear the screen
    exit        - Close the app.
                    
Catboy Commands:
    next    - Show a brand new url!
    save    - Save the url!
    exit    - Exit catboy mode.
"""


def exit_match():
    if True:
        print("", end="")
