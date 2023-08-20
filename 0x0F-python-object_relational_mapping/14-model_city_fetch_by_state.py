#!/usr/bin/python3
"""
Script that prints all City objects
from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create a connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        )
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all City objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print('{}: ({}) {}'.format(
            city.state.name, city.id, city.name
        ))
