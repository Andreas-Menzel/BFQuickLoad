import crud
from models import Preset
from database import create_db_and_tables

def seed_db():
    create_db_and_tables()
    presets = [
        Preset(name="Tinywhoop Air 65", description="Description for preset 1", tags=["freestyle", "5inch"], content="Content for preset 1", author="user1"),
        Preset(name="Eques DC", description="Description for preset 2", tags=["cinematic", "longrange"], content="Content for preset 2", author="user2"),
        Preset(name="Eques Squished", description="Description for preset 3", tags=["race", "quad"], content="Content for preset 3", author="user1"),
    ]
    for preset in presets:
        crud.create_preset(preset)
    print("Database seeded with dummy data.")

if __name__ == "__main__":
    seed_db()
