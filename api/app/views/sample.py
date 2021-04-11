from flask import Blueprint, jsonify
from flask_restful import Api, Resource

app = Blueprint('sample', __name__)
api = Api(app)

class SampleResource(Resource):

    def get(self, id):
        return jsonify({'result': 'Hello World. {}'.format(id)})


class SampleListResource(Resource):

    def get(self):
        return jsonify({'result': 'Hello List.'})


api.add_resource(SampleResource, '/samples/<string:id>')
api.add_resource(SampleListResource, '/samples/')