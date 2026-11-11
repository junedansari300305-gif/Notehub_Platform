from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from routes import notes_bp, colleges_bp, upload_bp  # ✅


app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(notes_bp)
app.register_blueprint(colleges_bp)
app.register_blueprint(upload_bp)

if __name__ == '__main__':
    app.run(debug=True)
