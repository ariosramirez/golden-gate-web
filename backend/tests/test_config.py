import pytest
from app import create_app, db
from app.models import SyncStatus


@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    # Use in-memory database for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def init_database(app):
    with app.app_context():
        if not SyncStatus.query.first():
            sync_status = SyncStatus(current_page=1)
            db.session.add(sync_status)
            db.session.commit()

