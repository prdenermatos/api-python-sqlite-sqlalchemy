from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)


app.config.from_object('config')
db = SQLAlchemy(app)




#Adicionar a cada novo controller 

from app.controllers.data_queries import *
from app.controllers.data_delete import *
from app.controllers.data_inserts import *
from app.controllers.data_update import *







