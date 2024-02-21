from flask import Flask
from flask_cors import CORS
from blueprints.tauri_releases import tauri_releases_bp
# Import the blueprint from routes/tauri_releases_bp.py

app = Flask(__name__)
CORS(app)

try:
    app.register_blueprint(tauri_releases_bp)
except Exception as e:
    print(e)
if __name__ == '__main__':
    app.run()