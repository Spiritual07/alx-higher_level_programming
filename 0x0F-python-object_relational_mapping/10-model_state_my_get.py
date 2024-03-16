#!/usr/bin/python3
"""  print state by name from the database hbtn_0e_0_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state(username, password, database_name, state_name):
    engine = create_engine(f"""mysql+mysqldb://{username}:{password}
                            @localhost:3306/{database_name}""")

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    print_state(username, password, database_name, state_name)
