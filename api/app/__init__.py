from flask import Flask
from .database import init_db
from .views import sample
import app.models

def create_app(config_name):
  app = Flask(__name__)

  # use config
  app.config.from_object('app.config.Config')

  # register application to blueprint.
  app.register_blueprint(sample.app, url_prefix = '/api')

  init_db(app)

  return app