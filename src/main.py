"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

@app.route('/people', methods= ['GET'])
    return jsonify(people)

@app.route('/people/<int:people_id>', methods= ['GET'])
    return jsonify(people)

@app.route('/planets', methods= ['GET'])
    return jsonify(planets)

@app.route('/planets/<int:planet_id>', methods= ['GET'])
    return jsonify()

@app.route('/users', methods= ['GET'])
    return jsonify()

@app.route('/users/favorites', methods= ['GET'])
    return jsonify()

@app.route('/favorite/planet/<int:planet_id>', methods= ['POST'])
    return jsonify()

@app.route('/favorite/people/<int:people_id>', methods= ['POST'])
    return jsonify()

@app.route('/favorite/planet/<int:planet_id>', methods= ['DELETE'])
    return jsonify()

@app.route('/favorite/people/<int:people_id>', methods= ['DELETE'])
    return jsonify()


if __name__ == '__main__':
PORT = int(os.environ.get('PORT', 3000))
app.run(host='0.0.0.0', port=PORT, debug=False)


