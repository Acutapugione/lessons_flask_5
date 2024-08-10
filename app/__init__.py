from flask import Flask
from db import Config

app = Flask(__name__)


from . import routes

if __name__ == "__main__":
    try:
        Config.up()
        app.run(
            host="localhost",
            port=5000,
            debug=True,
        )
    finally:
        Config.down()
