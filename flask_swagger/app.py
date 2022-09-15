from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app = Api(
    app=flask_app,
    version="1.0",
    title="Name Recorder",
    description="Manage names of various user of the application"
)

name_space = app.namespace('main', description='Main APIs')


@name_space.route("/<int:id>")
class MainClass(Resource):
    @app.doc(
        responses={
        200: 'OK',
        400: 'Invalid Argument',
        500: 'Mapping Key Error'},
        params={
            'id': 'Specify the Id associated with the person'
        }
    )
    def get(self):
        try:
            name = list_of_names[id]
            return {
                "status": "Person retrieved",
                "name": list_of_names[id]
            }
        except KeyError as e:
            name_space.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            name_space.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    def post(self):
        return {
            "status": "Posted new data"
        }

