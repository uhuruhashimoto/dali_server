from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

members = {"bob": 23}

class DaliMember(Resource):
    def get(self, name: str):
        return members[name]

api.add_resource(DaliMember, "/dalimember/<string:name>")

# Driver
if __name__ == "__main__":
    app.run(debug=True)