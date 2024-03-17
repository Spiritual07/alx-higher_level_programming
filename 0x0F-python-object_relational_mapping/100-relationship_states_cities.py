#!/usr/bin/python3
"""  Add state Louisiana to the database hbtn_0e_0_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def create_cal_and_sf(username, password, database_name):
    engine = create_engine(f"""mysql+mysqldb://{username}:{password}
                            @localhost:3306/{database_name}""")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    California = State(name="California")
    san_francisco = City(name="San Francisco", states=California)
    session.add(California)
    session.add(san_francisco)
    session.commit()

    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    create_cal_and_sf(username, password, database_name)
