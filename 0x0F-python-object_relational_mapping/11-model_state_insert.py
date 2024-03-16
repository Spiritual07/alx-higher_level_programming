#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, database_name):
    engine = create_engine(f"""mysql+mysqldb://{username}:{password}
                            @localhost:3306/{database_name}""")

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    print(louisiana.id)

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    add_state(username, password, database_name)
