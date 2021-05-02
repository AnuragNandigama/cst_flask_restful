from flask import Response, request
from database.models import Students
from flask_restful import Resource

class StudentsAPI(Resource):

    def get(self):
        student = Students.objects().to_json()
        return Response(student, mimetype="applicaiton/json", status=200)
    
    def post(self):
        body = request.get_json()
        student = Students(**body).save()
        id = student.s_id
        return {'id': str(id)}, 200
    
    
class SingleStudentAPI(Resource):
    
    def get(self, id):
        student = Students.objects.get(s_id=id).to_json()
        return Response(student, mimetype="applicaiton/json", status=200)

    def put(self, id):
        body = request.get_json()
        Students.objects.get(s_id=id).update(**body)
        return 'Student updated', 200
    
    def delete(self, id):
        Students.objects.get(s_id=id).delete()
        return Response("Student Deleted Successfully", mimetype="applicaiton/json", status=200)