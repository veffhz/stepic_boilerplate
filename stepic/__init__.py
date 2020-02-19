from flask import Flask
from flask.helpers import get_debug_flag

from stepic.extensions import db, migrate
from config import ProdConfig, DevConfig


CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = Flask(__name__)
app.config.from_object(CONFIG)

db.init_app(app)
migrate.init_app(app, db)

import stepic.controllers  # noqa
