#!/bin/bash

echo "To run this you must have python, pip and sqlite3 installed, check if they're installed."
echo -n "Continue? (Y/n) "
read -r ANSWER

case $ANSWER in
  y)
    echo "Continuing."
  ;;
  *)
    echo "See you later."
    exit 0
  ;;
esac

cd ./src/data || exit

touch users.db

sqlite3 users.db << 'END_SQL'
CREATE TABLE Users (UserName TEXT NOT NULL PRIMARY KEY, Password TEXT NOT NULL, Liked TEXT);
END_SQL

cd ../../

python -m venv anv

source anv/bin/activate
pip install -r requirements.txt

