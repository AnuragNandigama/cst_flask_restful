from .mcit import StudentsAPI, SingleStudentAPI

def initialize_route(api):
    api.add_resource(StudentsAPI, '/students')
    api.add_resource(SingleStudentAPI, '/students/<id>')
    