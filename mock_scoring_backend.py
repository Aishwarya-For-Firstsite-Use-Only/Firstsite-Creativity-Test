from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/score', methods=['POST'])
def score_drawings():
    data = request.get_json()

    drawings = data.get("drawings", [])
    text_answers = data.get("text", {})

    # Example heuristic scoring:
    fluency = 0
    flexibility = 0
    elaboration = 0
    originality = 0
    values = 0

    # Drawings is a list of dicts with strokes
    for drawing in drawings:
        strokes = drawing.get("strokes", [])
        stroke_count = len(strokes)
        # Fluency: more strokes = higher fluency (max 10)
        fluency += min(10, stroke_count // 5)

        # Flexibility: count distinct drawing questions, just mock 5 per drawing
        flexibility += 5

        # Originality: random guess (could be improved with AI)
        originality += 6

        # Elaboration: more strokes -> more detail
        elaboration += min(10, stroke_count // 8)

    # Average by number of drawings to normalize
    n = max(len(drawings), 1)
    fluency = min(10, fluency // n)
    flexibility = min(10, flexibility // n)
    elaboration = min(10, elaboration // n)
    originality = min(10, originality // n)

    # Values: score based on unique keywords in text answers (mock)
    all_text = " ".join(text_answers.values()).lower()
    keywords = ['agile', 'creative', 'inclusive', 'responsible']
    values = sum(word in all_text for word in keywords) * 2
    values = min(10, values)

    scores = {
        "fluency": fluency,
        "flexibility": flexibility,
        "elaboration": elaboration,
        "originality": originality,
        "values": values
    }

    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
