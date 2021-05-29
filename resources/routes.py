from .mcit import StudentsAPI, SingleStudentAPI, RegisterAPI, LoginAPI

def initialize_route(api):
    api.add_resource(StudentsAPI, '/students')
    api.add_resource(SingleStudentAPI, '/students/<id>')
    api.add_resource(RegisterAPI, '/auth/register')
    api.add_resource(LoginAPI, '/auth/login')
    