#!/usr/bin/python3
""" prints the first State object from the database """
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
    result = session.query(State).first()
    if result is None:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))
    session.close()
