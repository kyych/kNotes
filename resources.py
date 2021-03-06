from flask_restful import Resource, reqparse
from models import UserModel, RevokedTokenModel, NotesModel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
get_jwt_identity, get_raw_jwt)
from flask import redirect, url_for, make_response, session

parser = reqparse.RequestParser()

parser.add_argument('username', help='This field cannot be blank', required=False)
parser.add_argument('password', help='This field cannot be blank', required=False)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':'User {} already exists'.format(data['username'])}

        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity= data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            # return {
            #     'message':'User {} was created'.format(data['username']),
            #     'access_token':access_token,
            #     'refresh_token':refresh_token
            # }
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('access_token',access_token, httponly=True)
            resp.set_cookie('refresh_token',refresh_token, httponly=True)
            session['username'] = data['username']
            #return redirect(url_for('dashboard', messages="test"))
            return resp
        except:
            return {'message':'Something went wrong'},500

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message':'User {} doesnt exists'.format(data['username'])}

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity= data['username'])
            session['username'] = data['username']
            return {
                'message':'Logged in as {} '.format(current_user.username),
                'access_token':access_token,
                'refresh_token':refresh_token
            }
        else:
            return {'message':'Wrong password'}      
      
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message':'Access token has been revoked'}
        except:
            return {'message':'Something went wrong'},500      
      
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message':'Refresh token has been revoked'}
        except:
            return {'message':'Something went wrong'},500
      
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_refresh_token(identity = current_user)
        return {'access_token': access_token}
         
class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()
         
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }

class AddNote(Resource):
    def post(self):
        data = parser.parse_args()
        
        new_note = NotesModel(
            note = "Simple note for testing purposes",
            user = UserModel.find_by_username(session['username'])
        )
        try:
            new_note.save_to_db()
        except Exception as e:
            return {'message':'Something went wrong: {}'.format(e)}

        return {"message":"AddNoteReturn"}


