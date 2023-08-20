#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
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

    # Create a new State "California" and City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Add the City to the State's cities relationship
    new_state.cities.append(new_city)

    # Add the State and City objects to the session
    session.add(new_state)
    session.add(new_city)

    # Commit the changes
    session.commit()
