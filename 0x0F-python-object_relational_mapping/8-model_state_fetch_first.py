#!/usr/bin/python3
"""
A script that prints the first State object
from hbtn_0e_6_usa table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    init = session.query(State).first()
    if init is None:
        print("Nothing")
    else:
        print(init.id, init.name, sep=": ")
