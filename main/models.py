from main import db
import enum


class ProcedureEnum(enum.Enum):
    vaccination = "vaccination"
    treatment = "treatment"


class Animal(db.Model):
    animal_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    species = db.Column(db.String(30))
    breed = db.Column(db.String(30))
    birth_date = db.Column(db.DateTime())
    procedures = db.relationship("Procedure", backref="animal", lazy="dynamic")

    def __repr__(self):
        return f"animal with name {self.name}"


class Procedure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.Integer, db.ForeignKey("animal.animal_id"))
    date = db.Column(db.DateTime())
    type = db.Column(db.Enum(ProcedureEnum))
    drug = db.Column(db.String(30))

    def __repr__(self):
        return f"{self.type} procedure from {self.date} animal {self.animal}"
