from flask import Flask
from extensions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///defects.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

from routes.dashboard_routes import dashboard_bp
from routes.defect_routes import defect_bp

app.register_blueprint(dashboard_bp)
app.register_blueprint(defect_bp)


if __name__ == "__main__":
    app.run(debug=True)