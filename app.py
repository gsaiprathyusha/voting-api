from flask import Flask,jsonify
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return {"message" : "Deployed!"}

api.add_resource(Home, "/")


#app.run(debug=True)