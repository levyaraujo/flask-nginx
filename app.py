from flask import Flask, request
from src.app.useCases import PersonUseCases
from src.infra.Repository import PersonRepository
from src.infra.db import create_tables


def create_app():
    app = Flask(__name__)
    repo = PersonRepository()
    person_use_cases = PersonUseCases(repo)

    @app.before_request
    def before_request():
        return create_tables()

    @app.route("/")
    def home():
        return {"Hello": "World"}

    @app.route("/pessoas", methods=["POST"])
    def create_person():
        data = request.json
        return person_use_cases.create_person(data)

    return app
