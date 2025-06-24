from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/score', methods=['POST'])
def score_drawings():
    data = request.get_json()
    drawings = data.get("drawings", [])

    # Mock scoring logic: Random scores between 6 and 10
    scores = {
        "fluency": random.randint(6, 10),
        "flexibility": random.randint(6, 10),
        "elaboration": random.randint(6, 10),
        "originality": random.randint(6, 10),
        "values": random.randint(6, 10)
    }

    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
