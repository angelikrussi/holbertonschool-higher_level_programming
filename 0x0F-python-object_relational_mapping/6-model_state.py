#!/usr/bin/python3
'''
class definition of a State and an instance Base = declarative_base():
    '''


if __name__ == "__main__":
    import sys
    from model_state import Base, State

    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)