from flask import Flask, redirect, url_for
import os

from config import Config
from models.database import mysql

from routes.auth import auth_bp
from routes.tasks import tasks_bp

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.from_object(Config)

mysql.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)