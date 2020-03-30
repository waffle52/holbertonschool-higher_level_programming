#!/usr/bin/python3
""" lists all State objects that contain the letter a from the database """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()
    result = session.query(
        State).filter(State.name.ilike('%a%')).order_by(asc(State.id))
    for x in result:
        print("{}: {}".format(x.id, x.name))

    session.close()
