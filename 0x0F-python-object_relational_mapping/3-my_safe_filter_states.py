#!/usr/bin/python3
"""Take in argument and display it's value from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


def list_states(username, password, database_name, match):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    match = sys.argv[4]

    list_states(username, password, database_name, match)
