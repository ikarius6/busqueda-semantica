from flask import Flask, request, jsonify
from main import suggest_categories # Assuming your main.py and this new file are in the same directory

app = Flask(__name__)

@app.route('/suggest', methods=['GET'])
def suggest_category_api():
    """
    Flask endpoint to suggest categories based on input text.
    Expects a 'text' query parameter.
    e.g., /suggest?text=Hacemos platillos deliciosos
    """
    input_text = request.args.get('text')

    if not input_text:
        return jsonify({"error": "Missing 'text' parameter in query string"}), 400

    try:
        suggestions = suggest_categories(input_text)
        return jsonify({"input_text": input_text, "suggestions": suggestions})
    except Exception as e:
        # Log the exception for debugging
        print(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Make sure to set debug=False in a production environment
    app.run(debug=True, port=5001)