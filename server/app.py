from flask import Flask, make_response
from flask_restful import Api, Resource
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager


from server.extensions import db, migrate
from server.models import User, Guest, Episode, Appearance
from server.controllers.guest_controller import Guests
from server.controllers.episode_controller import Episodes, EpisodeByID

load_dotenv()

# replace with env var in production
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

app = Flask(__name__)
app.config.from_prefixed_env()

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)


class Home(Resource):
    def get(self):

        return {"message": "Hello, World!"}


api.add_resource(Home, '/')
api.add_resource(Episodes, "/episodes")
api.add_resource(EpisodeByID, "/episodes/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=5555)
