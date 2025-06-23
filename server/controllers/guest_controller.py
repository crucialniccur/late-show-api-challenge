from flask_restful import Resource
from flask import request
from server.models.guest import Guest
from server.extensions import db


class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [g.to_dict() for g in guests], 200
