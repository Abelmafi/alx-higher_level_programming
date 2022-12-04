#!/usr/bin/python3
""" This script lists all State objects with the name passed as
argument from database hbtn_0e_6_usa """
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                           format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states in session.query(State):
        print("{}: {}".format(states.id, states.name))
        result = session.query(City).filter(City.state_id == states.id)
        for city in result:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
