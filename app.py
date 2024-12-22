from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config, TestConfig
app = Flask(__name__)

if os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object(TestConfig)
    print("Using TestConfig ")
else:
    app.config.from_object(Config)
    print("Using Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
