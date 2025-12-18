from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin #to_dict, serilize_rule, serialize_only

# serialize_rule => what information to exclude
# serialize_only => what information to include

db = SQLAlchemy()

student_courses = db.Table('student_courses',
db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

# define model class => inheriting from db.Model

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-posts.user',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    # one user has many posts
    posts = db.relationship('Post', back_populates='user', lazy=True)

    

    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String(250))

    # one user has many posts
    # each foreign key links a post to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # each post belongs to one user
    user = db.relationship('User', back_populates='posts')

class Student(db.Model, SerializerMixin):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # many to many relationship with course
    courses = db.relationship('Course', secondary=student_courses, back_populates='students')


class Course(db.Model, SerializerMixin):
    __tablename__='courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)

    # many to many relationship with Student
    students = db.relationship('Student', secondary=student_courses, back_populates='courses')

    

    # {
    # "username" : "Jabir":
    # "id" : 1,
    # "email" : "maximum recursion depth exceedjabir@gmail.com",
    # "password" : "1234",
    # "posts" : [
    #     {
    #         "id": 5,
    #         "title": "The river between",
    #         "description" : "bbbbbbbbbb",
    #         "user" : {
    #             "username" : "Jabir":
    #             "id" : 1,
    #             "email" : "maximum recursion depth exceedjabir@gmail.com",
    #             "password" : "1234",
    #             "posts": [
    #                 {

    #                 }
    #             ]
    #         }
    #     }
    # ]
    # }



    