from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from database.database_init import db
from endpoints.mon_compte import ns

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'
app.config['CORS_RESSOURCES'] = {r'mon_compte/': {"origins": "*"}}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_budget.db'

db.init_app(app)

api = Api(app)
api.add_namespace(ns)


if __name__ == '__main__':
    app.run()
