from flask import Response, request
from flask_jwt_extended.view_decorators import jwt_required
from database.models import Students, User
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token

class StudentsAPI(Resource):

    @jwt_required
    def get(self):
        student = Students.objects().to_json()
        return Response(student, mimetype="applicaiton/json", status=200)
    
    @jwt_required
    def post(self):
        body = request.get_json()
        student = Students(**body).save()
        id = student.s_id
        return {'id': str(id)}, 200
    
    
class SingleStudentAPI(Resource):
    
    @jwt_required
    def get(self, id):
        student = Students.objects.get(s_id=id).to_json()
        return Response(student, mimetype="applicaiton/json", status=200)

    @jwt_required
    def put(self, id):
        body = request.get_json()
        Students.objects.get(s_id=id).update(**body)
        return 'Student updated', 200
    
    @jwt_required
    def delete(self, id):
        Students.objects.get(s_id=id).delete()
        return Response("Student Deleted Successfully", mimetype="applicaiton/json", status=200)
    
class RegisterAPI(Resource):
    
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200
        #return {'message': 'User Successfully Registered'}, 200
    
class LoginAPI(Resource):
    
    def post(self):
        body = request.get_json()
        user = User.objects.get(email = body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Invalid Credentials'}, 401
        expiry = datetime.timedelta(days=1)
        accesss_token = create_access_token(identity=str(user.id), expires_delta=expiry)
        return {'token': accesss_token}, 200