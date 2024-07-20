import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    database_path = os.path.join(os.getcwd(), 'images_data', 'images.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    with app.app_context():
        from .models import SyncStatus  # Import SyncStatus model
        from . import routes, models  # Import routes and models to register with the app
        db.create_all()
        if not SyncStatus.query.first():
            sync_status = SyncStatus(current_page=1)
            db.session.add(sync_status)
            db.session.commit()

    return app

app = create_app()  # Create an instance of the app
