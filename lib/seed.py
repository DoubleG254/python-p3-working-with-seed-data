#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the Game model from the models module
from models import Game

if __name__ == '__main__':
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Create instances of the Game model
    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)

    # Create a list of dictionaries for bulk_save_objects
    game_data = [
        {"title": "Breath of the Wild", "platform": "Switch", "genre": "Adventure", "price": 60},
        {"title": "Final Fantasy VII", "platform": "Playstation", "genre": "RPG", "price": 30},
        {"title": "Mario Kart 8", "platform": "Switch", "genre": "Racing", "price": 50},
    ]

    # Use bulk_save_objects to add the games to the database
    session.bulk_save_objects([Game(**data) for data in game_data])
    session.commit()

   
