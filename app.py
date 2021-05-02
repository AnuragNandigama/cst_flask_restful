from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_route

app= Flask(__name__)
api = Api(app)

DB_ATLAS_URI = "mongodb+srv://cst_user:mcit123@cluster0.vo3fn.mongodb.net/mcit?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_ATLAS_URI

initialize_db(app)
initialize_route(api)

app.run()