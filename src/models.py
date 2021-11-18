from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    rotation_period = db.Column(db.String, nullable=False)
    orbital_period = db.Column(db.String, nullable=False)
    diameter = db.Column  (db.String, nullable=False)
    climate = db.Column (db.String, nullable=False)
    gravity = db.Column (db.String, nullable=False)
    terrain = db.Column (db.String, nullable=False)
    surface_water = db.Column (db.String, nullable=False)
    population = db.Column (db.String, nullable=False)
    residents = db.Column (db.String, nullable=False)
    img_url = db.Column (db.String, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            name = self.name,
            rotation_period = self.rotation_period,
            orbital_period = self.orbital_period,
            diameter = self.diameter,
            climate = self.climate,
            gravity = self.gravity,
            terrain =self.terrain,
            surface_water = self.surface_water,
            population = self.population,
            residents = self.residents,
            img_url = self.img_url
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height  = db.Column(db.String, nullable=False)
    mass  = db.Column(db.String, nullable=False)
    hair_color  = db.Column(db.String, nullable=False)
    skin_color  = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year  = db.Column(db.String, nullable=False)
    gender  = db.Column(db.String, nullable=False)
    homeworld  = db.Column(db.String, nullable=False)
    species  = db.Column(db.String, nullable=False)
    vehicles  = db.Column(db.String, nullable=False)
    starships = db.Column(db.String, nullable=False)
    img_url  = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            height  = self.height,
            mass  = self.mass,
            hair_color  = self.hair_color,
            skin_color  = self.skin_color,
            eye_color = self.eye_color,
            birth_year  = self.birth_year,
            gender  = self.gender,
            homeworld  = self.homeworld,
            species  = self.species,
            vehicles  = self.vehicles,
            starships = self.starships,
            img_url  = self.img_url
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    model  = db.Column(db.String, nullable=False)
    manufacturer  = db.Column(db.String, nullable=False)
    cost_in_credits  = db.Column(db.String, nullable=False)
    length  = db.Column(db.String, nullable=False)
    max_atmosphering_speed  = db.Column(db.String, nullable=False)
    crew   = db.Column(db.String, nullable=False)
    passengers  = db.Column(db.String, nullable=False)
    cargo_capacity  = db.Column(db.String, nullable=False)
    consumables = db.Column(db.String, nullable=False)
    hyperdrive_rating  = db.Column(db.String, nullable=False)
    starship_class  = db.Column(db.String, nullable=False)
    pilots  = db.Column(db.String, nullable=False)
    img_url  = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return {
            name = self.name,
            model  = self.model,
            manufacturer  = self.manufacturer,
            cost_in_credits  = self.cost_in_credits,
            length  = self.length,
            max_atmosphering_speed  = self.max_atmosphering_speed, 
            crew   = self.crew,
            passengers  = self.passengers,
            cargo_capacity  = self.cargo_capacity,
            consumables = self.consumables,
            hyperdrive_rating  = self.hyperdrive_rating,
            starship_class  = self.starship_class,
            pilots  = self.pilots,
            img_url  = self.img_url
        }

class Favorite_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    user = db.relationship('User')
    planet = db.relationship('Planets')

    def __repr__(self):
        return '<Favorite_Planets %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class Favorite_Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    user = db.relationship('User')
    character = db.relationship('Characters')

    def __repr__(self):
        return '<Favorite_Characters %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class Favorite_Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    user = db.relationship('User')
    vehicle = db.relationship('Vehicles')

    def __repr__(self):
        return '<Favorite_Vehicles %r>' % self.user_id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id
        }

