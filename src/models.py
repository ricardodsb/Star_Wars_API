from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    users_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    favorites_planets = db.relationship("Favorites_planets")
    favorites_people = db.relationship("Favorites_people")

class Planets(db.Model):
    __tablename__='planets'
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(30), nullable=False)
    favorites_planets = db.relationship("Favorites_planets")

    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name
        }

class People(db.Model):
    __tablename__='people'
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(30), nullable=False)
    favorites_people = db.relationship("Favorites_people")

    def __repr__(self):
        return 'People %r>' % self.people_name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.people_name
        }
    

class Favorites_planets(db.Model):
    __tablename__='favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    planets_id = db.Column(db.String, db.ForeignKey('planets.id'), nullable=False)

    def __repr__(self):
        return '<Fav_planet %r>' % self.users_id

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "planets_id": self.planets_id
        }

class Favorites_people(db.Model):
    __tablename__='favorites_people'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.String, db.ForeignKey('users.id'))
    people_id = db.Column(db.String, db.ForeignKey('people.id'))

    def __repr__(self):
        return '<favorites_people %r>' % self.users_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.users_id,
            "people_id": self.people_id
        }