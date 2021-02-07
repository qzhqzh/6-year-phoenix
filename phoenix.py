import os
import sys

from flask import Flask
from . import models, routes, services


def create_app(config_name='settings.DevConfig'):
    project_dir = os.getcwd()
    sys.path.insert(0, project_dir)
    app = Flask(__name__)
    app.config.from_object(config_name)
    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    return app
