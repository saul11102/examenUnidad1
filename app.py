from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import config.config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.config.Config')
    db.init_app(app)
    with app.app_context():
        
        from models.cuenta import Cuenta
        from models.escultura import Escultura
        from models.persona import Persona

        from routes.route_persona import api_persona
        from routes.route_cuenta import api_cuenta
        from routes.route_escultura import api_escultura

        app.register_blueprint(api_persona)
        app.register_blueprint(api_cuenta)
        app.register_blueprint(api_escultura)

        #crear tablas de bd
        db.create_all()
        
    return app
