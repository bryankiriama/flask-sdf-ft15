from flask import Flask, make_response
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

# database configurations
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///school.db'

migrate = Migrate(app, db)

# initialize flask app to us db
db.init_app(app)



@app.route('/')
def index():
    return '<h1>INTRODUCTION TO FLASK APP</h1>'

@app.route('/about')
def about():
    return '<h3>This is now about us page</h3>'

@app.route('/profile/<string:username>')
def profile(username):
    return f'<h2>This profile belongs to {username}</h2>'

@app.route('/users')
def get_all_users():
    return make_response([user.to_dict() for user in User.query.all()])


if __name__ == '__main__':
    app.run(port=5555, debug=True)