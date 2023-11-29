from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:num>', methods=['GET'])
def check_prime(num):
    result = {
        "Number": num,
        "isPrime": is_prime(num)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)


"""from flask import Flask, jsonify

app = Flask(__name__)

# Simple airport data source (replace this with a database or external API)
airport_data = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    # Add more airport data as needed
}

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    airport_info = airport_data.get(icao_code.upper())

    if airport_info:
        response = {
            "ICAO": icao_code.upper(),
            "Name": airport_info["Name"],
            "Location": airport_info["Location"]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)"""

