from flask import Flask, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config.from_prefixed_env()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)


class Home(Resource):
    def get(self):

        return {"message": "Hello, World!"}


api.add_resource(Home, '/')

if __name__ == "__main__":
    app.run(debug=True, port=5555)
