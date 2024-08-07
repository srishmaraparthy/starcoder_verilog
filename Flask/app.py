from flask import Flask, request, jsonify
from inference import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    user_input = data.get('input', '')

    if user_input:
        try:
            # Generate system prompt and obtain prediction
            prediction = predict(user_input)
            
            
            return jsonify({
                "generated_text": prediction
            })
        except Exception as e:
            print(e)
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "No input provided"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
