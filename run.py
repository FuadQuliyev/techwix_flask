from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from admin import *
from app import *

main = Flask(__name__)

main.register_blueprint(admin)
main.register_blueprint(app)

db = SQLAlchemy(main)
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
migration = Migrate(main)


if __name__ == "__main__":
    main.run(debug=True)