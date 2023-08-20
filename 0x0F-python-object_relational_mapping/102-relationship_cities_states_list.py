#!/usr/bin/python3

"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

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

    # Query for all City objects and their corresponding State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        state_name = city.state.name
        print('{}: {} -> {}'.format(city.id, city.name, state_name))
