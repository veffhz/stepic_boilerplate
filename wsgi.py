from logging import Logger
from stepic import app

logger = Logger(__name__)
PORT = app.config['APP_PORT']

if __name__ == "__main__":
    if app.debug:
        logger.info(f'START APP ADMIN on http://localhost:{PORT}')
        app.run(port=PORT, threaded=True, use_reloader=True)
    else:
        app.run(port=PORT)
