from flask import Flask

from flask.helpers import get_debug_flag
from config import ProdConfig, DevConfig


CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = Flask(__name__)
app.config.from_object(CONFIG)

import stepic.controllers  # noqa
