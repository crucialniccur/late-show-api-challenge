from flask_restful import Resource
from flask import request
from server.models.appearance import Appearance
from server.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class Appearances(Resource):

    @jwt_required()
    def post(self):
        data = request.get_json()

        rating = data.get('rating')
        guest_id = data.get('guest_id')
        episode_id = data.get('episode_id')

        if not rating or not guest_id or not episode_id:
            return {"error": "Missing data"}, 400

        try:
            new_appearance = Appearance(
                rating=rating, guest_id=guest_id, episode_id=episode_id)
            db.session.add(new_appearance)
            db.session.commit()

            return {
                "id": new_appearance.id,
                "rating": new_appearance.rating,
                "guest_id": new_appearance.guest_id,
                "episode_id": new_appearance.episode_id
            }, 201
        except Exception as e:
            return {"error": str(e)}, 400
