from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    try:
        if request.method == 'POST':
            total_sqft = float(request.form['total_sqft'])
            location = request.form['location']
            bhk = int(request.form['bhk'])
            bath = int(request.form['bath'])
        else:  # Handle GET request
            total_sqft = float(request.args.get('total_sqft'))
            location = request.args.get('location')
            bhk = int(request.args.get('bhk'))
            bath = int(request.args.get('bath'))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except (TypeError, ValueError) as e:
        response = jsonify({
            'error': 'Invalid input',
            'message': str(e)
        })
        response.status_code = 400
        return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)