#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    result = engine.execute('SELECT states.name, cities.id, cities.name \
                            FROM cities, states \
                            WHERE states.id = cities.state_id')
    rows = result.fetchall()
    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
    result.close()
