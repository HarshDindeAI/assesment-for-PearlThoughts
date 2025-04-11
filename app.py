from flask import Flask, request, jsonify
from generator import generate_physician_linkedin_post
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def submit():
    data = request.get_json()

    response = generate_physician_linkedin_post(
        article_summary=data.get("article_summary",""),
        perspectives=data.get("perspectives",[  ]),
        url=data.get("url", None),
    )

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
