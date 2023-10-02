from ..infra.Repository import PersonRepository
from flask import request, jsonify, Response, make_response
from typing import Dict


class PersonUseCases:
    def __init__(self, repo: PersonRepository):
        self.repo = repo
        self.response = Response()

    def create_person(self, data: Dict):
        nickname = data.get("apelido")
        name = data.get("nome")
        birthday = data.get("nascimento")
        stack = data.get("stack")
        if not self.repo.person_exists(nickname):
            person = self.repo.create_person(nickname, name, birthday, stack)
            response = make_response(jsonify({"created": person.nickname}), 201)
            response.headers["Location"] = f"/pessoas/{person.id}"
            return response
        return jsonify({"Unprocessable Entity": f"User {nickname} already exists"}), 422

    def get_person_by_id(self, person_id):
        try:
            person = self.repo.get_person_by_id(person_id)
            if not person:
                return jsonify({"error": "Person not found"}), 404
            return jsonify({"person": person.__dict__})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def update_person(self, person_id):
        try:
            data = request.json
            name = data.get("name")
            birthday = data.get("birthday")
            stack = data.get("stack")

            if not name and not birthday and not stack:
                return jsonify({"error": "No data to update"}), 400

            person = self.repo.get_person_by_id(person_id)
            if not person:
                return jsonify({"error": "Person not found"}), 404

            updated_person = self.repo.update_person(person, name, birthday, stack)
            return jsonify(
                {
                    "message": "Person updated successfully",
                    "person": updated_person.__dict__,
                }
            )
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete_person(self, person_id):
        try:
            person = self.repo.get_person_by_id(person_id)
            if not person:
                return jsonify({"error": "Person not found"}), 404

            self.repo.delete_person(person)
            return jsonify({"message": "Person deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
