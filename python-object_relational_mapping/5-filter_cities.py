#!/usr/bin/python3
""" 5-filter_cities module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                FROM cities AS c \
                INNER JOIN states AS s \
                ON c.state_id = s.id")
    print(', '.join([row[2] for row in cur.fetchall() if row[4] == argv[4]]))
