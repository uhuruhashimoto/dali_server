from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import json

# Start Server
app = Flask(__name__)
api = Api(app)

# Argument Parsing
member_put_args = reqparse.RequestParser()
# member_put_args.add_argument("name", type=str, help="Name of the DALI member is required", location='form', required=True)
member_put_args.add_argument("year", type=str, help="Graduation year of the DALI member is required", location='form', required=True)
member_put_args.add_argument("dev", type=bool, help="DALI member dev [true/false] is required", location='form', required=True)
member_put_args.add_argument("des", type=bool, help="DALI member des [true/false] is required", location='form', required=True)
member_put_args.add_argument("pm", type=bool, help="DALI member pm [true/false] is required", location='form', required=True)
member_put_args.add_argument("core", type=bool, help="DALI member core [true/false] is required", location='form', required=True)
member_put_args.add_argument("mentor", type=bool, help="DALI member mentor [true/false] is required", location='form', required=True)
member_put_args.add_argument("major", type=str, help="Major of the DALI member is required", location='form', required=True)
member_put_args.add_argument("minor", type=str, help="Minor of the DALI member is required", location='form', required=True)
member_put_args.add_argument("birthday", type=str, help="Birthday [mm-dd] of the DALI member is required", location='form', required=True)
member_put_args.add_argument("home", type=str, help="Home [city, state] of the DALI member is required", location='form', required=True)
member_put_args.add_argument("quote", type=str, help="Quote is required", location='form', required=True)
member_put_args.add_argument("favorite thing 1", type=str, help="Favorite thing 1 is required", location='form', required=True)
member_put_args.add_argument("favorite thing 2", type=str, help="Favorite thing 2 is required", location='form', required=True)
member_put_args.add_argument("favorite thing 3", type=str, help="Favorite thing 3 is required", location='form', required=True)
member_put_args.add_argument("favorite dartmouth tradition", type=str, help="Favorite Dartmouth tradition is required", location='form', required=True)
member_put_args.add_argument("fun fact", type=str, help="Fun fact is required", location='form', required=True)
member_put_args.add_argument("picture", type=str, help="Picture url is required", location='form', required=True)

# Load file data and store by sequential ID
filename = "dali_social_media.json"
name_keyword = "name"
members = {}
f = open(filename)
memberlist = json.load(f)
for i in range(len(memberlist)):
    if name_keyword in memberlist[i]:
        members[(i, memberlist[i][name_keyword])] = memberlist[i]
    else:
        Error.log("Discarding entry. No name found in memberlist entry " + memberlist[i])
print(members)
f.close()

# Endpoints
class DaliMember(Resource):

    def get(self, id: int):
        for k in members.keys():
            if k[0] == id:
                return members[(k)]
        return {"message": "No user of id " + str(id)}

    def get(self, name: str):
        for k in members.keys():
            if k[1] == name:
                return members[(k)]
        return {"message": "No user of name " + name}

    def put(self, name: str):
        args = member_put_args.parse_args()
        new_id = len(members.keys())
        members[(new_id,name)] = args
        return members[(new_id, name)]

# Assemble API
api.add_resource(DaliMember, "/dalimember/<string:name>")

# Driver
if __name__ == "__main__":
    app.run(debug=True)