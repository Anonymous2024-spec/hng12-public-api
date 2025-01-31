from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)

# Enable CORS
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    return jsonify({
        "email": "nanashifah2@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Anonymous2024-spec/hng12-public-api.git"
    })
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from Render, default to 5000
    app.run(host='0.0.0.0', port=port)