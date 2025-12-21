from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

# database configurations
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///school.db'

migrate = Migrate(app, db)

# initialize flask app to us db
db.init_app(app)

# USER ROUTES

@app.route('/users', methods=['GET'])
def get_all_users():
    return make_response([user.to_dict() for user in User.query.all()], 200)

@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    if user:
        return make_response(user.to_dict(), 200)
    else:
        return make_response({'error': f'User not found'}, 404)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password')
    )
    db.session.add(new_user)
    db.session.commit()
    return make_response(new_user.to_dict(), 201)

@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    # data = request.get_json()
    user = User.query.get(id)
    if not user:
        return make_response({'error': f'User of id {id} not found'}, 404)
    data = request.get_json()

    if 'username' in data:
        user.username = data.get('username')
    if 'email' in data:
        user.email = data.get('email')
    if 'password' in data:
        user.password = data.get('password')

    db.session.commit()
    return make_response(user.to_dict(), 200)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return make_response({'error': f'User deleted sucessfull'}, 404)
    db.session.delete(user)
    db.session.commit()
    return make_response({}, 204)







@app.route('/')
def index():
    return '<h1>INTRODUCTION TO FLASK APP</h1>'

# @app.route('/about')
# def about():
#     return '<h3>This is now about us page</h3>'

# @app.route('/profile/<string:username>')
# def profile(username):
#     return f'<h2>This profile belongs to {username}</h2>'

# @app.route('/users')
# def get_all_users():
#     return make_response([user.to_dict() for user in User.query.all()])


if __name__ == '__main__':
    app.run(port=5555, debug=True)