from flask_restful import Resource
from . import api


class Status(Resource):
    def get(self):
        return {
            "status": "Up and running"
        }, 200

api.add_resource(Status, '/status')

