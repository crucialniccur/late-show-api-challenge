from flask import Flask, make_response
from flask_restful import Api, Resource
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from server.extensions import db, migrate
from server.models import User, Guest, Episode, Appearance
from server.controllers.guest_controller import Guests
from server.controllers.episode_controller import Episodes, EpisodeByID
from server.controllers.appearance_controller import Appearances

from server.controllers.auth_controller import auth_bp


load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
migrate.init_app(app, db)
jwt = JWTManager(app)

api = Api(app)


class Home(Resource):
    def get(self):
        return {"message": "Hello, World!"}


api.add_resource(Home, '/')
api.add_resource(Episodes, "/episodes")
api.add_resource(EpisodeByID, "/episodes/<int:id>")
api.add_resource(Appearances, "/appearances")


app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5555)
