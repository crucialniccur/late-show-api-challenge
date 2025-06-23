from server.extensions import db
from sqlalchemy_serializer import SerializerMixin


class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship(
        "Appearance", backref="episode", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Episode #{self.number} - {self.date}>"

    def to_dict_with_appearances(self):
        data = self.to_dict()
        data["appearances"] = [a.to_dict() for a in self.appearances]
        return data
