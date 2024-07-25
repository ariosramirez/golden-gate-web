import pytest
from flask import Flask
from flask_cors import CORS


class TestAppCreation:
    def test_app_instance(self, app):
        assert app is not None
        assert isinstance(app, Flask)

    def test_sqlalchemy_setup(self, app):
        assert 'SQLALCHEMY_DATABASE_URI' in app.config
        assert app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite:///')
