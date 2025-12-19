flask => light weight microframework
<!-- how hweb works -->
client  => request    response <= server   wsgi      flask/python application

http => GET, POST, PUT, PATCH, DELETE
STATUS CODE => 100, 200, 300, 400, 500
URL = https://moringaschool.com/about-us
ip address => 192.168.1.100


WSGI => Werkzeug
<!-- Database interaction -->
orm => flask sqlalchemy
    =>flask migrations

<!-- sqlalchemy relationships -->
primary => identifies a row in database table
foreign key => primary key to another table

many to many reelationship => associate table
seerialize data
 =>sqlalchemy-serializer => SerializerMixin
 serialize_rule => what data to exclude
 serialize_only => what data to include

 to_dict => rule && only arguments

 <!-- this is to avoid recursion depth -->


 API ENDPOINTS
 <!-- Users -->

 GET / USERS 