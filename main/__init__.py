from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config.Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from main import routes, models  # noqa: E402, F401
