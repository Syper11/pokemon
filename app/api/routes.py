from flask import Blueprint, request
from ..models import User
from ..apiauthhelper import basic_auth
from flask_cors import cross_origin

api = Blueprint('api', __name__)


@api.route('/api/signup', methods=["POST"])
def signupAPI():
    data = request.json

    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    email = data['email']
    password = data['password']
            

            # add user to database
    user = User(first_name, last_name, username, email, password)

    user.saveToDB()

    return {
        'status': 'ok',
        'message': "Succesffuly created an account!"
    }


@api.route('/api/login', methods=["POST"])
@basic_auth.login_required
def getToken():
    user = basic_auth.current_user()
    return {
        'status': 'ok',
        'user': user.to_dict(),
    }


