import flask
from flask_restful import Resource

from rest_utils import json_response
from services.groups_service import *


class GroupResource(Resource):
    @staticmethod
    def get(g_id):
        res = get_group(g_id)
        return json_response(res)

    @staticmethod
    def put(g_id):
        g_name = flask.request.json["g_name"]
        update_group(g_id, g_name)

    @staticmethod
    def delete(g_id):
        delete_group(g_id)
