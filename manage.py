import os

from config import config
from app import create_app


flask_env = os.getenv('FLASK_ENV')

app = create_app(config=config[flask_env])


if __name__ == "__main__":
    app.run()
