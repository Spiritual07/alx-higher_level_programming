#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from model_city import City
from sqlalchemy.orm import sessionmaker


def print_state_by_city(username, password, database_name):
    engine = create_engine(f"mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{database_name}")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = session.query(State.name)\
                    .filter(State.id == city.state_id).scalar()
        print(f"{state_name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    print_state_by_city(username, password, database_name)
