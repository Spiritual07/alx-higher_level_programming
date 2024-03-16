#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def list_states(username, password, database_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                    INNER JOIN states ON states.id=cities.state_id
                    WHERE states.name=%s""", (sys.argv[4],))
    rows = cursor.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=', ')

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
