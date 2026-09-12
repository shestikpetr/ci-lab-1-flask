from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return jsonify(status="ok"), 200

    @app.route("/greet/<name>")
    def greet(name):
        if not name.strip():
            return jsonify(error="name is required"), 400
        if len(name) > 50:
            return jsonify(error="name is too long"), 400
        return jsonify(message=f"Hello, {name}!"), 200

    return app
