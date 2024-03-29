#!/usr/bin/python3
"""Script to Filter States"""
import MySQLdb
import sys


def filter_states():
    """Filter states from database by listing all states
    with a name starting with N (upper N)
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Define Connection Parameter"""
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC"
                )
    myrows = cur.fetchall()
    for row in myrows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    filter_states()
