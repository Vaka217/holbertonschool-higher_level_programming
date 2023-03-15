#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name = 'Louisiana'))
    session.commit()
    result = session.query(State).order_by(State.id.desc()).first()
    print(result.id)
