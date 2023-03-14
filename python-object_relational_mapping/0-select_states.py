#!/usr/bin/python3
""" 0-select_states module"""
from sys import argv
import MySQLdb


def select_states():
    """ lists all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    select_states()
