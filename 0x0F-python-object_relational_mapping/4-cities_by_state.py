#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb


def list_states(username, password, database_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states ON states.id=cities.state_id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
