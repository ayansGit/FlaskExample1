from flask import Flask, jsonify, request
#from flask_jwt import JWT, jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from werkzeug.security import safe_str_cmp

from security import authenticate, identity, getUser
from demo import getStores
from user import User


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

#jwt = JWT(app, authenticate, identity) #/auth

stores = [
    {
    "name": "Store 1",
    "items": [
        {
            "name": "item 1",
            "price": 20
        },
        {
            "name": "item 2",
            "price": 30
        }
    ]
    }
]

@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    user =  User.find_by_username(username)
    if user and safe_str_cmp(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify({
            "success": True,
            "data": user,
            "message": "Logged in successfully",
            "access_token": access_token})
    else:
         return jsonify({
             "success": False,
             "message": "User not found"}), 404

@app.route("/register", methods = ["POST"])
def register():
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    fullname = request_data["fullname"]
    phone = request_data["phone"] 
    user = User.check_if_user_exist(username, phone)

    if user:
        return jsonify({
             "success": False,
             "message": "User already exists"}), 400
    else:
        try:
            User.register(fullname, phone, username, password)
        except:
            return jsonify({
                "success": False,
                "message": "Something went wrong during register"}), 500
        
        user =  User.find_by_username(username)
        if user:
            access_token = create_access_token(identity=username)
            return jsonify({
                "success": True,
                "data": user,
                "message": "Registered successfully",
                "access_token": access_token})
        else:
            return jsonify({
                "success": False,
                "message": "Something went wrong during register"}), 500

    



@app.route("/storelist")
@jwt_required()
def getMyList():
    return jsonify({"stores": stores})

@app.route("/user", methods=["POST"])
def getUser():
    data = request.get_json()
    username = data["username"]
    res =  User.find_by_username(username)
    return jsonify({"user":  res})


# if __name__ == "__main__":
#     app.run(debug=False)