#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb;
from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

ipdb.set_trace()
