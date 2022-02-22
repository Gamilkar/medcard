from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config.Configuration)

from main import routes  # noqa: E402, F401
