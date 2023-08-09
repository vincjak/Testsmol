from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)