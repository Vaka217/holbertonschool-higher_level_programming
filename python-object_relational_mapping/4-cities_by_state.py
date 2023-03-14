#!/usr/bin/python3
""" 2-my_filter_states module"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT ROW_NUMBER() OVER(), \
                cities.name,states.name \
                FROM cities, states \
                WHERE state_id = states.id")
    [print(row) for row in cur.fetchall()]
