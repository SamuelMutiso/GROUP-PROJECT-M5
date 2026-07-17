
from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app)

    @app.route("/api/health")
    def health():
        return jsonify({"status": "ok"})

    # Blueprints get registered here as each route file is built, e.g.:
    # from routes.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix="/api")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
