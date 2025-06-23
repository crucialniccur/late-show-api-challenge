from server.app import app, db
from server.models import User, Guest, Episode, Appearance
from faker import Faker
import random

fake = Faker()


def seed():
    with app.app_context():
        # Clear existing data
        Appearance.query.delete()
        Guest.query.delete()
        Episode.query.delete()
        User.query.delete()

        # Seed Users
        users = [User(username=fake.user_name()) for _ in range(5)]
        db.session.add_all(users)

        # Seed Guests
        guests = [Guest(name=fake.name(), occupation=fake.job())
                  for _ in range(10)]
        db.session.add_all(guests)

        # Seed Episodes
        episodes = [Episode(date=str(fake.date_this_decade()),
                            number=i+1) for i in range(10)]
        db.session.add_all(episodes)
        db.session.commit()

        # Seed Appearances
        for _ in range(20):
            appearance = Appearance(
                rating=random.randint(1, 5),
                guest_id=random.choice(guests).id,
                episode_id=random.choice(episodes).id
            )
            db.session.add(appearance)

        db.session.commit()
        print("Database seeded!")


if __name__ == "__main__":
    seed()
