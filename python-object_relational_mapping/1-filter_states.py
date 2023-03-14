#!/usr/bin/python3
""" 1-filter_states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE SUBSTRING(name, 1, 1) = 'N'")
    [print(row) for row in cur.fetchall()]
