#!/usr/bin/env python3

import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game



if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    import ipdb; ipdb.set_trace()
