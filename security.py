from models.user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload): #identity is unique to flask jwt that we install
    user_id = payload['identity']#payload is the content of the JWT token
    return UserModel.find_by_id(user_id)
