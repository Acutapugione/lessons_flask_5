from app import app
from db import Config, migrate

if __name__ == "__main__":
    try:
        Config.up()
        migrate()
        app.run(
            host="localhost",
            port=5000,
            debug=True,
        )
    finally:
        Config.down()
