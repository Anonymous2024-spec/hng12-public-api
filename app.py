from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

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
    app.run(debug=True)