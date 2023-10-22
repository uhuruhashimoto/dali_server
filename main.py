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
    year = db.Column(db.String(100))
    dev = db.Column(db.Boolean)
    des = db.Column(db.Boolean)
    pm = db.Column(db.Boolean)
    core = db.Column(db.Boolean)
    mentor = db.Column(db.Boolean)
    major = db.Column(db.String(100))
    minor = db.Column(db.String(100))
    birthday = db.Column(db.String(100))
    home = db.Column(db.String(100))
    quote = db.Column(db.String(100))
    favorite_thing_1 = db.Column(db.String(100))
    favorite_thing_2 = db.Column(db.String(100))
    favorite_thing_3 = db.Column(db.String(100))
    favorite_tradition = db.Column(db.String(100))
    fun_fact = db.Column(db.String(100))
    picture = db.Column(db.String(100))

    def __repr__(self):
        return f"id = {self.id}\n"\
        f"name = {self.name}\n"\
        f"year = {self.year}\n"\
        f"dev = {self.dev}\n"\
        f"des = {self.des}\n"\
        f"pm = {self.pm}\n"\
        f"core = {self.core}\n"\
        f"mentor = {self.mentor}\n"\
        f"major = {self.major}\n"\
        f"minor = {self.minor}\n"\
        f"birthday = {self.birthday}\n"\
        f"home = {self.home}\n"\
        f"quote = {self.quote}\n"\
        f"favorite thing 1 = {self.favorite_thing_1}\n"\
        f"favorite thing 2 = {self.favorite_thing_2}\n"\
        f"favorite thing 3 = {self.favorite_thing_3}\n"\
        f"favorite tradition = {self.favorite_tradition}\n"\
        f"fun fact = {self.fun_fact}\n"\
        f"picture = {self.picture}"

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'year': fields.String,
    'dev': fields.Boolean,
    'des': fields.Boolean,
    'pm': fields.Boolean,
    'core': fields.Boolean,
    'mentor': fields.Boolean,
    'major': fields.String,
    'minor': fields.String,
    'birthday': fields.String,
    'home': fields.String,
    'quote': fields.String,
    'favorite_thing_1': fields.String,
    'favorite_thing_2': fields.String,
    'favorite_thing_3': fields.String,
    'favorite_tradition': fields.String,
    'fun_fact': fields.String,
    'picture': fields.String,
}

# STATEFUL; DO NOT USE EXCEPT AT SERVER START UP
# with app.app_context():
#     db.create_all()
# END STATEFUL CODE

# Argument Parsing
member_put_args = reqparse.RequestParser()
member_put_args.add_argument("name", type=str, help="Name of the DALI member is required", location='form', required=True)
member_put_args.add_argument("year", type=str, help="Graduation year of the DALI member is required", location='form', required=True)
member_put_args.add_argument("dev", type=inputs.boolean, help="DALI member dev [true/false] is required", location='form', required=True)
member_put_args.add_argument("des", type=inputs.boolean, help="DALI member des [true/false] is required", location='form', required=True)
member_put_args.add_argument("pm", type=bool, help="DALI member pm [true/false] is required", location='form', required=True)
member_put_args.add_argument("core", type=bool, help="DALI member core [true/false] is required", location='form', required=True)
member_put_args.add_argument("mentor", type=bool, help="DALI member mentor [true/false] is required", location='form', required=True)
member_put_args.add_argument("major", type=str, help="Major of the DALI member is required", location='form', required=True)
member_put_args.add_argument("minor", type=str, help="Minor of the DALI member is required", location='form')
member_put_args.add_argument("birthday", type=str, help="Birthday [mm-dd] of the DALI member is required", location='form', required=True)
member_put_args.add_argument("home", type=str, help="Home [city, state] of the DALI member is required", location='form', required=True)
member_put_args.add_argument("quote", type=str, help="Quote is required", location='form', required=True)
member_put_args.add_argument("favorite thing 1", type=str, help="Favorite thing 1 is required", location='form', required=True)
member_put_args.add_argument("favorite thing 2", type=str, help="Favorite thing 2 is required", location='form', required=True)
member_put_args.add_argument("favorite thing 3", type=str, help="Favorite thing 3 is required", location='form', required=True)
member_put_args.add_argument("favorite dartmouth tradition", type=str, help="Favorite Dartmouth tradition is required", location='form', required=True)
member_put_args.add_argument("fun fact", type=str, help="Fun fact is required", location='form', required=True)
member_put_args.add_argument("picture", type=str, help="Picture url is required", location='form', required=True)


# Endpoints
class DaliMembers(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = DaliMemberModel.query.all()
        if not result:
            abort(404, message = "No existing members.")
        return result

class DaliMemberByID(Resource):
    @marshal_with(resource_fields)
    def get(self, member_id: int):
        result = DaliMemberModel.query.filter_by(id=member_id).first()
        if not result:
            abort(404, message = f"No existing member of id {member_id}")
        return result

    @marshal_with(resource_fields)
    def post(self, member_id: int):
        args = member_put_args.parse_args()
        result = DaliMemberModel.query.filter_by(id=member_id).first()
        if result:
            abort(409, message = f"Cannot create new member because member exists with id {member_id}")
        member = DaliMemberModel(
                id=member_id,
                name=args['name'],
                year = args['year'],
                dev=args['dev'],
                des = args['des'],
                pm = args['pm'],
                core = args['core'],
                mentor = args['mentor'],
                major = args['major'],
                minor = args['minor'],
                birthday = args['birthday'],
                home = args['home'],
                quote = args['quote'],
                favorite_thing_1 = args['favorite thing 1'],
                favorite_thing_2 = args['favorite thing 2'],
                favorite_thing_3 = args['favorite thing 3'],
                favorite_tradition = args['favorite dartmouth tradition'],
                fun_fact = args['fun fact'],
                picture = args['picture']
            )
        db.session.add(member)
        db.session.commit()
        return member

class DaliMemberByFullName(Resource):
    @marshal_with(resource_fields)
    def get(self, member_name: str):
        result = DaliMemberModel.query.filter_by(name=member_name).first()
        if not result:
            abort(404, message = f"No existing member of name {member_name}")
        return result

class DaliMemberByFirstName(Resource):
    @marshal_with(resource_fields)
    def get(self, member_name: str):
        q = member_name + '%'
        result = DaliMemberModel.query.filter(DaliMemberModel.name.like(q)).all()
        if not result:
            abort(404, message = f"No existing member of name {member_name}")
        return result

class DaliMemberByLastName(Resource):
    @marshal_with(resource_fields)
    def get(self, member_name: str):
        q = '%' + member_name
        result = DaliMemberModel.query.filter(DaliMemberModel.name.like(q)).all()
        if not result:
            abort(404, message = f"No existing member of name {member_name}")
        return result

class DaliMemberAttributeByName(Resource):
    def get(self, member_name: str, member_attribute: str):
        result = DaliMemberModel.query.filter_by(name=member_name).first()
        if not result:
            abort(404, message = f"No existing member of name {member_name}")
        if member_attribute not in  result.__dict__.keys() or member_attribute not in resource_fields.keys():
            abort(404, message = f"No attribute of name {member_attribute} found for {member_name}")
        return {member_attribute : result.__dict__[member_attribute]}

class DaliMembersByClassYear(Resource):
    @marshal_with(resource_fields)
    def get(self, class_year: int):
        s = str(class_year)
        result = DaliMemberModel.query.filter_by(year=s).all()
        if not result:
            abort(404, message = f"No existing member with year {class_year}")
        return result

def filter_bool(val: str):
    mappings = {
        '0': False,
        'false': False,
        'False': False,
        '1': True,
        'true': True,
        'True': True
    }
    if val in mappings:
        return mappings[val]
    abort(404, message="Invalid true/false input provided.")

class DaliMembersByDes(Resource):
    @marshal_with(resource_fields)
    def get(self, des: str):
        des = filter_bool(des)
        result = DaliMemberModel.query.filter_by(des=des).all()
        if not result:
            abort(404, message = f"No existing DES members found for query.")
        return result

class DaliMembersByDev(Resource):
    @marshal_with(resource_fields)
    def get(self, dev: str):
        dev = filter_bool(dev)
        result = DaliMemberModel.query.filter_by(dev=dev).all()
        if not result:
            abort(404, message = f"No existing DEV members found for query.")
        return result

class DaliMembersByPM(Resource):
    @marshal_with(resource_fields)
    def get(self, pm: str):
        pm = filter_bool(pm)
        result = DaliMemberModel.query.filter_by(pm=pm).all()
        if not result:
            abort(404, message = f"No existing PM members found for query.")
        return result

class DaliMembersByCore(Resource):
    @marshal_with(resource_fields)
    def get(self, core: str):
        core = filter_bool(core)
        result = DaliMemberModel.query.filter_by(core=core).all()
        if not result:
            abort(404, message = f"No existing Core members found for query.")
        return result

class DaliMembersByMentor(Resource):
    @marshal_with(resource_fields)
    def get(self, mentor: str):
        mentor = filter_bool(mentor)
        result = DaliMemberModel.query.filter_by(mentor=mentor).all()
        if not result:
            abort(404, message = f"No existing Mentor members found for query.")
        return result


# Assemble API
api.add_resource(DaliMembers, "/dalimember")
api.add_resource(DaliMemberByID, "/dalimember/<int:member_id>")
api.add_resource(DaliMemberByFullName, "/dalimember/<string:member_name>")
api.add_resource(DaliMemberAttributeByName, "/dalimember/<string:member_name>/<string:member_attribute>")
api.add_resource(DaliMemberByFirstName, "/dalimember/search/firstname/<string:member_name>/")
api.add_resource(DaliMemberByLastName, "/dalimember/search/lastname/<string:member_name>/")
api.add_resource(DaliMembersByClassYear, "/dalimember/search/year/<int:class_year>/")
api.add_resource(DaliMembersByDes, "/dalimember/search/des/<string:des>/")
api.add_resource(DaliMembersByDev, "/dalimember/search/dev/<string:dev>/")
api.add_resource(DaliMembersByPM, "/dalimember/search/pm/<string:pm>/")
api.add_resource(DaliMembersByCore, "/dalimember/search/core/<string:core>/")
api.add_resource(DaliMembersByMentor, "/dalimember/search/mentor/<string:mentor>/")

# Driver
if __name__ == "__main__":
    app.run(debug=True)