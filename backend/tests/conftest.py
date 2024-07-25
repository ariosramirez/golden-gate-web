import os
import pytest
import requests_mock
from requests_mock_flask import add_flask_app_to_mock
from app import create_app, db
from app.models import SyncStatus
from flask_cors import CORS


UNSPLASH_API_KEY = 'test_unsplash_api_key'


@pytest.fixture(scope='module')
def app():
    os.environ['UNSPLASH_API_KEY'] = UNSPLASH_API_KEY
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def init_database(app):
    with app.app_context():
        if not SyncStatus.query.first():
            sync_status = SyncStatus(current_page=1)
            db.session.add(sync_status)
            db.session.commit()
