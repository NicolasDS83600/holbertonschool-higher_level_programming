#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(City, State).join(State).order_by(City.id).all()

        for city, state in result:
            print(f"{state.name}: ({city.id}) {city.name}")
    finally:
        session.close()
