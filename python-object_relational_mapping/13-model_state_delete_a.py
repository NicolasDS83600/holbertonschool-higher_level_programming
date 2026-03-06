#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states_to_delete = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .all()
        )
        for state in states_to_delete:
            session.delete(state)
        session.commit()
    finally:
        session.close()
