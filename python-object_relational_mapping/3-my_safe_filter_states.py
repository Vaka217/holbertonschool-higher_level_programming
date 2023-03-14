#!/usr/bin/python3
""" 2-my_filter_states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (argv[4],))
    [print(row) for row in cur.fetchall()]
