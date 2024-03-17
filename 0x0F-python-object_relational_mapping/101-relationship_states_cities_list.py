#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_state_and_city(username, password, database_name):
    engine = create_engine(f"mysql+mysqldb://{username}:{password}\
                            @localhost:3306/{database_name}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

list_state_and_city(username, password, database_name)
