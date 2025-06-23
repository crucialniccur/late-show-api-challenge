from flask_restful import Resource
from flask import request
from server.models.guest import Guest
from server.extensions import db


class Guest(Resource):
    def get(self):

        guest = Guest.query.all()

        return [g.to_dict() for g in guest], 200
