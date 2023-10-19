from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import json

# Start Server
app = Flask(__name__)
api = Api(app)

# Argument Parsing
member_put_args = reqparse.RequestParser()
member_put_args.add_argument("name", type=str, help="Name of the DALI member")

# Data (placeholder)
filename = "dali_social_media.json"
f = open(filename)
members = json.load(f)
f.close()

# Endpoints
class DaliMember(Resource):
    def get(self, name: str):
        return members

    def put(self, name: str):
        print(request.form)
        return members

# Assemble API
api.add_resource(DaliMember, "/dalimember/<string:name>")

# Driver
if __name__ == "__main__":
    app.run(debug=True)