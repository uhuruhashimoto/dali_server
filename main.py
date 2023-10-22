from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with, inputs
from flask_sqlalchemy import SQLAlchemy

# Start Server
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class DaliMemberModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # year = db.Column(db.String(100))
    dev = db.Column(db.Boolean)
    # des = db.Column(db.Boolean)
    # pm = db.Column(db.Boolean)
    # core = db.Column(db.Boolean)
    # mentor = db.Column(db.Boolean)
    # major = db.Column(db.String(100))
    # minor = db.Column(db.String(100))
    # birthday = db.Column(db.String(100))
    # home = db.Column(db.String(100))
    # quote = db.Column(db.String(100))
    # favorite_thing_1 = db.Column(db.String(100))
    # favorite_thing_2 = db.Column(db.String(100))
    # favorite_thing_3 = db.Column(db.String(100))
    # favorite_tradition = db.Column(db.String(100))
    # fun_fact = db.Column(db.String(100))
    # picture = db.Column(db.String(100))

    def __repr__(self):
        return f"id = {id}, name = {name}, dev = {dev}"

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'dev': fields.Boolean
}

# STATEFUL
# with app.app_context():
#     db.create_all()

# Argument Parsing
member_put_args = reqparse.RequestParser()
member_put_args.add_argument("name", type=str, help="Name of the DALI member is required", location='form', required=True)
# member_put_args.add_argument("year", type=str, help="Graduation year of the DALI member is required", location='form', required=True)
member_put_args.add_argument("dev", type=inputs.boolean, help="DALI member dev [true/false] is required", location='form', required=True)
# member_put_args.add_argument("des", type=inputs.boolean, help="DALI member des [true/false] is required", location='form', required=True)
# member_put_args.add_argument("pm", type=bool, help="DALI member pm [true/false] is required", location='form', required=True)
# member_put_args.add_argument("core", type=bool, help="DALI member core [true/false] is required", location='form', required=True)
# member_put_args.add_argument("mentor", type=bool, help="DALI member mentor [true/false] is required", location='form', required=True)
# member_put_args.add_argument("major", type=str, help="Major of the DALI member is required", location='form', required=True)
# member_put_args.add_argument("minor", type=str, help="Minor of the DALI member is required", location='form', required=True)
# member_put_args.add_argument("birthday", type=str, help="Birthday [mm-dd] of the DALI member is required", location='form', required=True)
# member_put_args.add_argument("home", type=str, help="Home [city, state] of the DALI member is required", location='form', required=True)
# member_put_args.add_argument("quote", type=str, help="Quote is required", location='form', required=True)
# member_put_args.add_argument("favorite thing 1", type=str, help="Favorite thing 1 is required", location='form', required=True)
# member_put_args.add_argument("favorite thing 2", type=str, help="Favorite thing 2 is required", location='form', required=True)
# member_put_args.add_argument("favorite thing 3", type=str, help="Favorite thing 3 is required", location='form', required=True)
# member_put_args.add_argument("favorite dartmouth tradition", type=str, help="Favorite Dartmouth tradition is required", location='form', required=True)
# member_put_args.add_argument("fun fact", type=str, help="Fun fact is required", location='form', required=True)
# member_put_args.add_argument("picture", type=str, help="Picture url is required", location='form', required=True)


# Endpoints
class DaliMember(Resource):
    @marshal_with(resource_fields)
    def get(self, member_id: int):
        result = DaliMemberModel.query.filter_by(id=member_id).first()
        if not result:
            abort(404, message = f"No existing member of id {member_id}")
        return result

    @marshal_with(resource_fields)
    def put(self, member_id: int):
        args = member_put_args.parse_args()
        result = DaliMemberModel.query.filter_by(id=member_id).first()
        if result:
            abort(409, message = f"Cannot create new member because member exists with id {member_id}")
        member = DaliMemberModel(id=member_id, name=args['name'], dev=args['dev'])
        db.session.add(member)
        db.session.commit()
        return member

# Assemble API
api.add_resource(DaliMember, "/dalimember/<int:member_id>")

# Driver
if __name__ == "__main__":
    app.run(debug=True)