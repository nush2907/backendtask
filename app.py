from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json['data']
    numbers = []
    alphabets = []
    highest_lowercase_alphabet = []

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower() and (not highest_lowercase_alphabet or item > highest_lowercase_alphabet[-1]):
                highest_lowercase_alphabet = [item]

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with your actual user ID
        "email": "john@xyz.com",          # Replace with your actual email
        "roll_number": "ABCD123",         # Replace with your actual roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)