from flask import Flask, jsonify
from flask_cors import CORS
import logging
from config import Config
from routes.api import api_bp

# Configure logging
logging.basicConfig(
    level=getattr(logging, Config.LOGGING_CONFIG['level']),
    format=Config.LOGGING_CONFIG['format'],
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for Angular frontend
CORS(app)

# Register blueprints
app.register_blueprint(api_bp, url_prefix='')

@app.route('/')
def index():
    """Root endpoint."""
    return jsonify({
        "message": "Mundial 2026 Hub API",
        "version": "1.0",
        "status": "running"
    })

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=Config.DEBUG
    )