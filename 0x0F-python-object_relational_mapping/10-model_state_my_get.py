#!/usr/bin/python3
""" prints the State object with the name passed as argument """
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
        State).filter(State.name == sys.argv[4]).first()
    if result is None:
        print("Not found")
    else:
        print("{}".format(result.id))

    session.close()
